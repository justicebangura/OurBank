import streamlit as st

# Dictionary to store user data
users = {}

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password")
            return False

def open_account():
    st.title("Open Account")
    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")
    
    if st.button("Open Account"):
        if username in users:
            st.warning("Username already exists!")
        else:
            users[username] = {"password": password, "balance": 0}
            st.success("Account opened successfully!")

def deposit():
    st.title("Deposit")
    username = st.text_input("Enter username")
    amount = st.number_input("Enter amount to deposit", min_value=0.0)
    
    if st.button("Deposit"):
        if username in users:
            users[username]["balance"] += amount
            st.success("Deposit successful!")
            st.info(f"New balance: {users[username]['balance']}")
        else:
            st.error("User not found")

def withdraw():
    st.title("Withdraw")
    username = st.text_input("Enter username")
    amount = st.number_input("Enter amount to withdraw", min_value=0.0)
    
    if st.button("Withdraw"):
        if username in users:
            if users[username]["balance"] >= amount:
                users[username]["balance"] -= amount
                st.success("Withdrawal successful!")
                st.info(f"New balance: {users[username]['balance']}")
            else:
                st.error("Insufficient balance")
        else:
            st.error("User not found")

def transfer():
    st.title("Transfer")
    sender = st.text_input("Enter your username")
    receiver = st.text_input("Enter receiver's username")
    amount = st.number_input("Enter amount to transfer", min_value=0.0)
    
    if st.button("Transfer"):
        if sender in users and receiver in users:
            if users[sender]["balance"] >= amount:
                users[sender]["balance"] -= amount
                users[receiver]["balance"] += amount
                st.success("Transfer successful!")
                st.info(f"New balance: {users[sender]['balance']}")
            else:
                st.error("Insufficient balance")
        else:
            st.error("One or both users not found")

def main():
    st.sidebar.title("Bank App")
    options = ["Login", "Open Account", "Deposit", "Withdraw", "Transfer"]
    choice = st.sidebar.selectbox("Menu", options)

    if choice == "Login":
        login()
    elif choice == "Open Account":
        open_account()
    elif choice == "Deposit":
        deposit()
    elif choice == "Withdraw":
        withdraw()
    elif choice == "Transfer":
        transfer()

if __name__ == "__main__":
    main()