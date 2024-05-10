import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Load the environment variables
def load_env():
    if load_dotenv():
        st.sidebar.text('env is loaded successfully')
    else:
        st.sidebar.text('Failed to load env')

# Connect to the Web3 provider
def connect_w3():
    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URI')))
    if w3.is_connected():
        st.sidebar.text('Connected to Ganache')
    else:
        st.sidebar.text('Failed to connect to Ganache')
    return w3

# Load the contract
@st.cache_resource()
def load_contract(_w3):
    with open(Path('cryptoWallet.json')) as f:
        CryptoWallet_abi = json.load(f)
    contract_address = os.getenv('SMART_CONTRACT_ADDRESS')
    contract = _w3.eth.contract(address= contract_address, abi=  CryptoWallet_abi)
    return contract

# Transfer Ether
def transfer_eth(my_account, to_address, amount):
    if Web3.is_address(to_address):
        tx_hash = w3.eth.send_transaction({
            'to': to_address,
            'from': my_account,
            'gas': 2000000,
            'gasPrice': w3.to_wei('20', 'gwei'),
            'value': w3.to_wei(amount, 'ether')
        })
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            st.write("Transaction complete.")
            st.write(f"The receipt hash is {receipt.transactionHash.hex()}")
    else:
        st.write("Please enter a valid recipient address.")

# Deposit Ether
def deposit_eth(contract, amount, sender_address):
    tx_hash = contract.functions.deposit().transact({'from': sender_address, 'value': int(amount * 10**18)})
    return tx_hash

# Withdraw Ether
def withdraw_eth(contract, amount, sender_address):
    tx_hash = contract.functions.withdraw(int(amount * 10**18)).transact({'from': sender_address})
    return tx_hash

# Check Balance
def check_balance(w3, account_address):
    try:
        balance = w3.eth.get_balance(account_address)
        return balance
    except Exception as e:
        st.write(f"Error occurred while fetching balance: {e}")
        return None

#Streamlit code 
    
if __name__ == "__main__":
    # Load environment variables
    load_env()

    # Connect to Web3 provider
    w3 = connect_w3()

    # Set default account
    default_account = "0x2F15A6E8902F70C104e39074806ef024D8aea092" 

    # Load contract
    contract = load_contract(w3)

    st.title("Crypto Wallet")

    # Deposit Ether
    st.subheader("Deposit Ether")
    deposit_amount = st.number_input("Enter deposit amount:")
    if st.button("Deposit"):
        tx_hash = deposit_eth(contract, deposit_amount, default_account)
        st.write(f"Transaction hash: {tx_hash.hex()}")

    # Withdraw Ether
    st.subheader("Withdraw Ether")
    withdraw_amount = st.number_input("Enter withdrawal amount:")
    if st.button("Withdraw"):
        tx_hash = withdraw_eth(contract, withdraw_amount, default_account)
        st.write(f"Transaction hash: {tx_hash.hex()}")

    # Transfer Ether
    st.subheader("Transfer Ether")
    transfer_amount = st.number_input("Enter transfer amount:")
    to_address = st.text_input("Enter recipient address:")
    if st.button("Transfer"):
        if Web3.is_address(to_address):
            tx_hash = transfer_eth(default_account, to_address, transfer_amount)
            if tx_hash is not None:
                st.write(f"Transaction complete. The receipt hash is {tx_hash.hex()}")
        else:
            st.write("Please enter a valid recipient address.")

    # Check Balance
    st.subheader("Check Balance")
    account_address = st.text_input("Enter account address:")
    if st.button("Check Balance"):
        if w3.is_address(account_address):
            balance = check_balance(w3, account_address)
            if balance is not None:
                st.write(f"Balance of {account_address}: {balance / 10**18} ETH")
        else:
            st.write("Invalid account address. Please provide a valid Ethereum address.")