import streamlit as st
from backend.banking_account import (
    open_new_account,
    login_user,
    get_account_balance,
    deposit_funds,
    withdraw_funds,
    transfer_funds,
)

# Function to log in and set session
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login_user(username, password):
            st.session_state['logged_in_user'] = username
            st.session_state['logged_in'] = True 
            st.success("Logged in successfully!")
            st.write("")  
            st.subheader("Redirecting to Account Operations page...")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to create a new account
def create_account():
    st.title("Open Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Create Account"):
        try:
            open_new_account(username, password)
            st.success("Account created successfully!")
            st.write("")
            st.subheader("Redirecting to Account Operations page...")
            st.experimental_rerun()
        except ValueError as e:
            st.warning(str(e))

# Function to handle account operations
def account_operations():
    username = st.session_state['logged_in_user']
    st.title(f"Welcome, {username}")

    # Logout button
    if st.button("Logout"):
        st.session_state['logged_in_user'] = None
        st.session_state['logged_in'] = False
        st.subheader("Logged out successfully!")
        st.experimental_rerun()

    # Get account balance directly
    account_balance = get_account_balance(username)
    st.write(f"Current balance: {account_balance:.2f}")

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
            st.write(f"Transfer successful! your new balance: {sender_balance:.2f}")
        except ValueError as e:
            st.error(str(e))
            
# Streamlit main function to handle menu and operations
def show():
    st.sidebar.title("Bank App")
    options = ["Account Operations", "Login", "Open Account"] 
    choice = st.sidebar.selectbox("Menu", options)

    if choice == "Account Operations":
        if st.session_state.get('logged_in', False): 
            account_operations()
        else:
            login()  
    elif choice == "Login":
        login()
    elif choice == "Open Account":
        create_account()

show()
