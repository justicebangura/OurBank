import os
import json
import logging
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import yfinance as yf
from forex_python.converter import CurrencyRates


# Load the environment variables
def load_env():
    if load_dotenv():
        st.sidebar.text("env loaded successfully")
    else:
        st.sidebar.text('Failed to load env')


# Connecting to ganache environment
def connect_ganache():
    # Connect to ganache using web3
    w3_ganache = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
    # Check for connection
    if w3_ganache.is_connected():
        st.sidebar.text("Connected to Ganache")
    else:
        st.sidebar.text("Failed to connect to Ganache")
    
    return w3_ganache

# Connecting to Sepolia testnet environment
def connect_sepolia():
    # Connect to sepolia using web3
    w3_sepolia = Web3(Web3.HTTPProvider(os.getenv("SEPOLIA_URL")))
    # Check for connection
    if w3_sepolia.is_connected():
        st.sidebar.text("Connected to Sepolia")
    else:
        st.sidebar.ttext("Failed to connect to Sepolia")
    
    return w3_sepolia



# Load the contract
@st.cache_resource()
def load_contract(_w3, abi_path, contract_address):
    with open(Path(abi_path)) as f:
        artWork_abi = json.load(f)
    
    contract_address= Web3.to_checksum_address(contract_address)
    
    contract = _w3.eth.contract(address = contract_address, abi = artWork_abi)
    return contract

# Increment function
def increment_number():
    st.session_state.number += 1



def convert_eth_to_other_currency():
    # Retrieve conversion info from sepolia contract
    conversion_rate = sepolia_contract.functions.getEthPrice().call()
    conversion_rate_decimal_corrected = conversion_rate / 1e8
    st.write(f"Currently, 1 Ehterum cost ${round(conversion_rate_decimal_corrected, 2)} USD")

    # Convert the amount of Ethereum to the desired currency
    eth_amount = st.number_input("Enter the amount of ETH")
    total_price_usd = conversion_rate_decimal_corrected * eth_amount
    to_currency = st.radio("Conver to", ['GBP', 'USD', 'EUR', 'JPY', 'CAD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY'], key = 'convert_to_other_currency')

    if st.button('Convert', key = 'Converting_eth_to_other_currencies'):
        c = CurrencyRates()
        result = c.convert('USD', to_currency, total_price_usd)
        st.write(f"{eth_amount} ETH is {result:.2f} {to_currency}")
    
    return conversion_rate

def get_stock_price(conversion_rate):
    stock_symbol = st.text_input('Please write the symbol of stock you would like to purchase')
    stock_symbol = stock_symbol.upper()
    n_of_stocks = st.number_input("Number of stocks you wish to purchase", min_value = 1, step = 1)
    
    if st.button("Today's price", on_click = increment_number):
        # Retrieve current price of the stock
        data = yf.Ticker(stock_symbol)
        price_data = data.history(period = '1d', interval = '1m')
        price_data = price_data['Close'].iloc[-1]
        st.write(f"Current price of {stock_symbol} is ${round(price_data, 2)} USD")
    
    if st.button("Price quote", on_click = increment_number):
        # Retrieve current price of the stock
        data = yf.Ticker(stock_symbol)
        price_data = data.history(period = '1d', interval = '1m')
        price_data = price_data['Close'].iloc[-1]
        
        # Calculate the amount of USD or ETH needed to purchase the stock
        total_price = n_of_stocks * price_data
        total_price_in_eth = total_price / (conversion_rate / 1e8)
        st.write(f"In order to buy {n_of_stocks} shares of {stock_symbol}, you need ${round(total_price, 2)} USD or {round(total_price_in_eth, 4)} ETH")
        st.write("Confirm purchase?")

        if st.button("Confirm", key = 'confirm_transaction', on_click = increment_number):
            st.write("Transaction has been completed.")

def transfer_eth(my_account):
    # Select the account that you want to send ETH to
    to_address = st.selectbox("Transfer to", w3_ganache.eth.accounts[1:])
    
    # Type the amount of ETH to send to
    amount = st.number_input("How much ETH to transfer?")
    
    # Transfer
    if st.button("Transfer", key = 'Transfer_eth'):
        tx_hash = w3_ganache.eth.send_transaction({
            'to': to_address,
            'from': my_account,
            'gas': 2000000,
            'gasPrice': w3_ganache.to_wei('20', 'gwei'),
            'value': w3_ganache.to_wei(amount, 'ether')
        })
        receipt = w3_ganache.eth.wait_for_transaction_receipt(tx_hash)
        st.write(f"Transaction complete. The receipt hash is {receipt}")


### All the functions below may not be necessary functions. Delete when confirmed

def deposit_ether(amount, my_account):
    tx_hash = ganache_contract.functions.deposit().transact({'from': my_account, 'value': w3_ganache.to_wei(amount, 'ether')})
    receipt = w3_ganache.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def send_ether(to_address, amount):
    tx_hash = ganache_contract.functions.send(to_address, w3_ganache.to_wei(amount, 'ether')).transact()
    receipt = w3_ganache.eth.wait_for_transaction_receipt(tx_hash)
    return receipt


#def transfer_eth(my_account):
    to_address = st.selectbox("Transfer to", w3_ganache.eth.accounts[1:])
    amount = st.number_input("How much ETH to transfer?")
    if st.button("Transfer", key = 'Transfer_eth'):
        deposit_ether(amount, my_account)
        receipt = send_ether(to_address, amount)
        st.write(f"Transaction complete. The receipt hash is {receipt}")

def convert_currency():
    amount = st.number_input('Enter the amount:', min_value=0.01, step=0.01, format="%.2f")
    from_currency = st.radio("From", ['GBP', 'USD', 'EUR', 'JPY', 'CAD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY'])
    to_currency = st.radio("Conver to", ['GBP', 'USD', 'EUR', 'JPY', 'CAD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY'])
    
    if st.button('Change'):
        c = CurrencyRates()
        result = c.convert(from_currency, to_currency, amount)
        st.write(f"{amount} {from_currency} is {result:.2f} {to_currency}")

def convert_Eth_to_Usd():
    # Retrieve conversion info from sepolia contract
    conversion_rate = sepolia_contract.functions.getEthPrice().call()
    conversion_rate_decimal_corrected = conversion_rate / 1e8
    st.write(f"Currently, 1 Ehterum cost ${round(conversion_rate_decimal_corrected, 2)} USD")
    
    # Enter the Ethereum amount so that it can convert the number of Ethereum to 
    eth_amount = st.number_input("Enter the amount of ETH you wish to convert")
    if st.button("Convert", on_click = increment_number):
        eth_to_usd = round(conversion_rate_decimal_corrected * eth_amount, 2)
        st.write(f"Your {eth_amount} ETH has been convered to ${eth_to_usd} USD")
    
    return conversion_rate





def main():
    if 'number' not in st.session_state:
        st.session_state.number = 0

    my_account = w3_ganache.eth.accounts[0]
    st.write(f"My account address: {my_account}")
    st.write(f"Account balance : {w3_ganache.eth.get_balance(w3_ganache.eth.accounts[0]) / 1e18} ETH")

    st.markdown("---")
    st.title("Convert ETH to other currencies")
    conversion_rate = convert_eth_to_other_currency()
    st.markdown("---")
    st.title("Buy stocks")
    get_stock_price(conversion_rate)
    st.markdown("---")
    st.title("Transfer ETH to different account")
    transfer_eth(my_account)

    



if __name__ == "__main__":
    st.sidebar.title('App status')
    load_env()
    w3_ganache = connect_ganache()
    w3_sepolia = connect_sepolia()
    accounts = w3_ganache.eth.accounts
    sepolia_contract = load_contract(w3_sepolia, './contracts/compiled/ethConvert_abi.json', os.getenv('SMART_CONTRACT_ADDRESS'))
    ganache_contract = load_contract(w3_ganache, './contracts/compiled/ganache_abi.json', os.getenv('SMART_CONTRACT_2_ADDRESS'))
    main()







