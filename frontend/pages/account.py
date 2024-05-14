import streamlit as st
import os
import time
from backend.banking_account import (
    open_new_account as new_acct,
    login_user,
    check_account_balance,
    deposit_funds,
    withdraw_funds,
    transfer_funds,
)

# Dictionary to store user sessions
if 'logged_in_user' not in st.session_state:
    st.session_state['logged_in_user'] = None


def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username", key = 'username')
    password = st.sidebar.text_input("Password", type="password", key = 'password')
    

    if st.sidebar.button("Login"):
        if login_user(username, password):
            st.session_state['logged_in_user'] = username
            st.success("Logged in successfully!")
            time.sleep(1)
            if st.session_state['selected_option'] == 'Open Account':
                st.session_state.selected_option = "Account Operations"
        else:
            st.error("Invalid username or password")

# Function to create a new account
def open_new_account():
    st.title("Open Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Create Account"):
        try:
            new_acct(username, password)
            st.success("Account created successfully!")
        except ValueError as e:
            st.warning(str(e))

# Function to handle account operations
def account_operations():
    username = st.session_state['logged_in_user']
    st.title(f"Welcome, {username}")
    
    # Get account details
    account_details = check_account_balance(username)
    account_balance_details = [f'{i[1]:.2f} {i[0]}' for i in account_details['balance'].items()]
    st.write(f"Current balance: ")
    for i in account_balance_details:
        st.write(i)
    

    # Transaction history
    st.subheader("Transaction History")
    for transaction in account_details['transactions']:
        st.write(f"{transaction['type'].capitalize()} of {transaction['amount']:.2f} {transaction['currency']} at {transaction['timestamp']}")

    # Deposit into account
    st.subheader("Deposit")
    amount = st.number_input("Enter amount to deposit", min_value=0.0)
    if st.button("Deposit"):
        new_balance = deposit_funds(username, amount)
        st.write(f"Deposit successful! New balance: $ {new_balance['USD']:.2f} USD")

    # Withdraw from account
    st.subheader("Withdraw")
    amount = st.number_input("Enter amount to withdraw", min_value=0.0)
    if st.button("Withdraw"):
        try:
            new_balance = withdraw_funds(username, amount)
            st.write(f"Withdrawal successful! $ New balance: {new_balance['USD']:.2f} USD")
        except ValueError as e:
            st.error(str(e))

    # Transfer to another user
    st.subheader("Transfer")
    receiver = st.text_input("Recipient's username")
    amount = st.number_input("Enter amount to transfer", min_value=0.0)
    if st.button("Transfer"):
        try:
            sender_balance, receiver_balance = transfer_funds(username, receiver, amount)
            st.write(f"Transfer successful! Sender's new balance: {sender_balance:.2f}")
        except ValueError as e:
            st.error(str(e))

# Streamlit main function to handle menu and operations
def show():
    
    st.sidebar.title("Bank App")
    options = ["Open Account", "Account Operations"]

    # Login and logout logic
    if st.session_state['logged_in_user']:
        logout = st.sidebar.button('Log out')
        if logout:
            st.write('Logged out successfully')
            st.session_state['logged_in_user'] = None
    else:
        login()

    choice = st.sidebar.selectbox("Menu", options, key = 'selected_option')

    # Account features dropdown
    if choice == "Open Account":
        open_new_account()
    elif choice == "Account Operations":
        if st.session_state['logged_in_user']:
            st.sidebar.title("Select account")
            account_options = ['Everyday account', 'Crypto account']
            choose_accounts = st.sidebar.selectbox("Select account", account_options)
            if choose_accounts == 'Everyday account':
                account_operations()
            elif choose_accounts == 'Crypto account':
                crypto_wallet()
        else:
            st.warning("Please log in first")
    



import streamlit as st
from solidity.files.crypto_wallet import (
    load_env,
    connect_ganache,
    connect_sepolia,
    load_contract,
    eth_exchange_info,
    convert_eth_to_other_currency,
    stock_info,
    transfer_eth,
    get_account_balance,
)

# Streamlit function to display the Account page
def crypto_wallet():
    # Load environment variables and connect to Ethereum networks
    load_env()
    w3_ganache = connect_ganache()
    w3_sepolia = connect_sepolia()

    # Load contracts
    ganache_contract = load_contract(
        w3_ganache, "./solidity/files/contracts/compiled/ganache_abi.json", os.getenv("SMART_CONTRACT_2_ADDRESS")
    )
    sepolia_contract = load_contract(
        w3_sepolia, "./solidity/files/contracts/compiled/ethConvert_abi.json", os.getenv("SMART_CONTRACT_ADDRESS")
    )
    username = st.session_state['logged_in_user']
    # Get user account details
    my_account = w3_ganache.eth.accounts[0]  # First account in Ganache
    bank_account = w3_ganache.eth.accounts[9]  # Sample bank account
    conversion_rate = eth_exchange_info(sepolia_contract)  # Get Ethereum conversion rate

    # Display account information
    st.title("Account Information")
    st.write(f"My Ethereum address: {my_account}")
    st.write(f"Account balance: {get_account_balance(w3_ganache, my_account):.2f} ETH")

    # Converting Ethereum to different currencies
    st.header("Convert Ethereum")
    eth_amount = st.number_input("Enter ETH amount to convert", min_value=0.01)
    currency = st.selectbox("Convert to", ["USD", "GBP", "EUR", "JPY", "CAD"])
    if st.button("Convert"):
        converted_value = convert_eth_to_other_currency(eth_amount, conversion_rate, currency)
        st.write(f"{eth_amount:.2f} ETH is {converted_value:.2f} {currency}")
        deposit_funds(username, converted_value, currency = currency)
        transfer_eth(w3_ganache, my_account, bank_account, eth_amount)

    # Transfer Ethereum to another account
    st.header("Transfer Ethereum")
    to_account = st.text_input("Recipient's Ethereum address")
    transfer_amount = st.number_input("ETH amount to transfer", min_value=0.01)
    if st.button("Transfer"):
        try:
            receipt = transfer_eth(w3_ganache, my_account, to_account, transfer_amount)
            st.success("Transfer successful!")
            st.write(f"Transaction hash: {receipt['transactionHash'].hex()}")
        except Exception as e:
            st.error(f"Transfer failed: {e}")

    # Stock information and interaction
    st.header("Stock Information")
    stock_symbol = st.text_input("Enter stock symbol")
    stock_symbol = stock_symbol.upper()
    num_of_stocks = st.number_input("How many stocks do you want to buy", min_value = 1, step = 1)
    if st.button("Get Stock Price"):
        stock_price, price_in_eth = stock_info(conversion_rate, stock_symbol)
        st.write(f"Current price for 1 share of {stock_symbol}: ${stock_price:.2f} USD or {price_in_eth:.4f} ETH")
        if num_of_stocks > 1:
            st.write(f"Price for {num_of_stocks} shares of {stock_symbol}: $ {stock_price * num_of_stocks:.2f} USD or {price_in_eth * num_of_stocks:.4f} ETH")
    if st.button("Purchase using ETH"):
        stock_price, price_in_eth = stock_info(conversion_rate, stock_symbol)
        transfer_eth(w3_ganache, my_account, bank_account, price_in_eth*num_of_stocks)
        st.write("Purchase complete")
    if st.button("Purchase with USD"):
        stock_price, price_in_eth = stock_info(conversion_rate, stock_symbol)
        remaining_balance = withdraw_funds(username, stock_price*num_of_stocks)
        st.write(f"Purchase complete. Remaining balance is $ {remaining_balance['USD']} USD")


    st.write(
        """
        Use the menu to navigate between different sections of the crypto bank. 
        You can manage your account, convert Ethereum, transfer funds, and interact with stocks.
        """
    )

# If this file is executed directly, run the 'show' function
if __name__ == "__main__":
    show()
