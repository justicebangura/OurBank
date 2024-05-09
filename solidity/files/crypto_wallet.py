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
        st.sidebar.text("Failed to connect to Sepolia")
    
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

# Shares and displays Ethereum exchange information
def eth_exchange_info():
    # Retrieve conversion info from sepolia contract
    conversion_rate = sepolia_contract.functions.getEthPrice().call()
    conversion_rate_decimal_corrected = conversion_rate / 1e8
    st.write(f"Currently, 1 Ehterum cost ${round(conversion_rate_decimal_corrected, 2)} USD")
    return conversion_rate


# Converting Ethereum to different currencies
def convert_eth_to_other_currency(my_account, bank_account, conversion_rate):    
    # Convert the amount of Ethereum to the desired currency
    eth_amount = st.number_input("Enter the amount of ETH")
    total_price_usd = (conversion_rate / 1e8) * eth_amount
    to_currency = st.radio("Conver to", ['GBP', 'USD', 'EUR', 'JPY', 'CAD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY'], key = 'convert_to_other_currency')

    # Display the exchanged amount in desired currency
    if st.button('Convert', key = 'Get_exchange_info'):
        c = CurrencyRates()
        result = c.convert('USD', to_currency, total_price_usd)
        st.write(f"{eth_amount} ETH is {result:.2f} {to_currency}")

    # Exchange Ethereum to desired currency
    if st.button('Exchange', key = 'Exchange_eth_to_other_currencies'):
        c = CurrencyRates()
        result = c.convert('USD', to_currency, total_price_usd)
        transfer_eth(my_account, bank_account, eth_amount)
        st.write("Money exchange complete")

        return {to_currency: result}
    

def stock_info(conversion_rate, stock_symbol, n_of_stocks):
    # Retrieve stock price information
    stock_symbol = stock_symbol.upper()
    data = yf.Ticker(stock_symbol)
    price_data = data.history(period = '1d', interval = '1m')
    price_data = price_data['Close'].iloc[-1]
    total_price = n_of_stocks * price_data
    total_price_in_eth = total_price / (conversion_rate / 1e8)
    return price_data, total_price_in_eth, total_price


def get_stock_price(my_account, bank_account, conversion_rate, stock_symbol, n_of_stocks):
    # Display current stock price info
    if st.button("Today's price", on_click = increment_number):
        price_data, total_price_in_eth, total_price = stock_info(conversion_rate, stock_symbol, n_of_stocks)
        st.write(f"Current price of 1 share of {stock_symbol} is ${round(price_data, 2)} USD or {round(total_price_in_eth/n_of_stocks, 4)} ETH")
        if n_of_stocks > 1:
            st.write(f"{n_of_stocks} shares of {stock_symbol} would equal to ${round(total_price, 2)} USD or {round(total_price_in_eth, 4)} ETH")
    
    # Purchase stocks using Ethereum
    if st.button("Purchase using Ethereum", on_click = increment_number):
        price_data, total_price_in_eth, total_price = stock_info(conversion_rate, stock_symbol, n_of_stocks)
        transfer_eth(my_account, bank_account, total_price_in_eth)
        st.write("Purchase complete, you will get rich in no time!")
        return {stock_symbol: n_of_stocks}
    
    # Purchase stocks using USD in bank account
    if st.button("Purchase using money in bank account"):
        price_data, total_price_in_eth, total_price = stock_info(conversion_rate, stock_symbol, n_of_stocks)
        st.write("Purchase complete, you will get rich in no time!")
        return {'USD': - total_price}, {stock_symbol: n_of_stocks}

def transfer_eth(my_account, to_address, amount):
    # Transfer
    tx_hash = w3_ganache.eth.send_transaction({
        'to': to_address,
        'from': my_account,
        'gas': 2000000,
        'gasPrice': w3_ganache.to_wei('20', 'gwei'),
        'value': w3_ganache.to_wei(amount, 'ether')
    })
    receipt = w3_ganache.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        st.write("Transaction complete.")
        st.write(f"The receipt hash is {receipt.transactionHash.hex()}")
    else:
        st.write("Please enter a valid recipient address.")

def transfer_eth_button(my_account):
    # Enter required information and operate transfer_eth function
    to_address = st.selectbox("Transfer to", w3_ganache.eth.accounts[1:])
    amount = st.number_input("How much ETH to transfer?")
    if st.button("Transfer", key = 'Transfer_eth'):
        transfer_eth(my_account, to_address, amount)








def main():
    if 'number' not in st.session_state:
        st.session_state.number = 0

    my_account = w3_ganache.eth.accounts[0]
    bank_account = w3_ganache.eth.accounts[9]
    st.write(f"My account address: {my_account}")
    st.write(f"Account balance : {w3_ganache.eth.get_balance(w3_ganache.eth.accounts[0]) / 1e18} ETH")
    conversion_rate = eth_exchange_info()

    st.markdown("---")
    st.title("Convert ETH to other currencies")
    result = convert_eth_to_other_currency(my_account, bank_account, conversion_rate)
    st.markdown("---")
    st.title("Buy stocks")
    stock_symbol = st.text_input('Please write the symbol of stock you would like to purchase')
    n_of_stocks = st.number_input("Number of stocks you wish to purchase", min_value = 1, step = 1)
    get_stock_price(my_account, bank_account, conversion_rate, stock_symbol, n_of_stocks)
    st.markdown("---")
    st.title("Transfer ETH to different account")
    transfer_eth_button(my_account)

    



if __name__ == "__main__":
    st.sidebar.title('App status')
    load_env()
    w3_ganache = connect_ganache()
    w3_sepolia = connect_sepolia()
    accounts = w3_ganache.eth.accounts
    sepolia_contract = load_contract(w3_sepolia, './contracts/compiled/ethConvert_abi.json', os.getenv('SMART_CONTRACT_ADDRESS'))
    ganache_contract = load_contract(w3_ganache, './contracts/compiled/ganache_abi.json', os.getenv('SMART_CONTRACT_2_ADDRESS'))
    main()







