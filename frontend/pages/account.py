import streamlit as st
from backend.banking_account import (
    open_new_account,
    login_user,
    check_account_balance,
    deposit_funds,
    withdraw_funds,
    transfer_funds,
)

# Dictionary to store user sessions
if 'logged_in_user' not in st.session_state:
    st.session_state['logged_in_user'] = None

# Function to log in and set session
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login_user(username, password):
            st.session_state['logged_in_user'] = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# Function to create a new account
def open_new_account():
    st.title("Open Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Create Account"):
        try:
            open_new_account(username, password)
            st.success("Account created successfully!")
        except ValueError as e:
            st.warning(str(e))

# Function to handle account operations
def account_operations():
    username = st.session_state['logged_in_user']
    st.title(f"Welcome, {username}")
    
    # Get account details
    account_details = check_account_balance(username)
    st.write(f"Current balance: {account_details['balance']:.2f}")

    # Transaction history
    st.subheader("Transaction History")
    for transaction in account_details['transactions']:
        st.write(f"{transaction['type'].capitalize()} of {transaction['amount']} at {transaction['timestamp']}")

    # Deposit into account
    st.subheader("Deposit")
    amount = st.number_input("Enter amount to deposit", min_value=0.0)
    if st.button("Deposit"):
        new_balance = deposit_funds(username, amount)
        st.write(f"Deposit successful! New balance: {new_balance:.2f}")

    # Withdraw from account
    st.subheader("Withdraw")
    amount = st.number_input("Enter amount to withdraw", min_value=0.0)
    if st.button("Withdraw"):
        try:
            new_balance = withdraw_funds(username, amount)
            st.write(f"Withdrawal successful! New balance: {new_balance:.2f}")
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
def main():
    st.sidebar.title("Bank App")
    options = ["Login", "Open Account", "Account Operations"]
    choice = st.sidebar.selectbox("Menu", options)

    if choice == "Login":
        login()
    elif choice == "Open Account":
        open_new_account()
    elif choice == "Account Operations":
        if st.session_state['logged_in_user']:
            account_operations()
        else:
            st.warning("Please log in first")


