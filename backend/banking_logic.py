import streamlit as st

# Mock user database (in a real application, you would use a proper database)
USER_DATABASE = {
    "user1": {"password": "password1", "balance": 1000},
    "user2": {"password": "password2", "balance": 2000}
}

def authenticate_user(username, password):
    if username in USER_DATABASE:
        if USER_DATABASE[username]["password"] == password:
            return True
    return False

def display_account_balance(username):
    st.write(f"Account Balance for {username}: ${USER_DATABASE[username]['balance']}")

def make_transaction(username, amount):
    USER_DATABASE[username]["balance"] += amount

def main():
    st.title("OUR BANK")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            display_account_balance(username)

            # Transaction options
            st.header("Make a Transaction")
            transaction_type = st.radio("Transaction Type", ("Deposit", "Withdraw"))
            amount = st.number_input("Amount")

            if st.button("Submit"):
                if transaction_type == "Deposit":
                    make_transaction(username, amount)
                    st.success(f"Deposit of ${amount} successful!")
                    display_account_balance(username)
                elif transaction_type == "Withdraw":
                    if amount <= USER_DATABASE[username]["balance"]:
                        make_transaction(username, -amount)
                        st.success(f"Withdrawal of ${amount} successful!")
                        display_account_balance(username)
                    else:
                        st.error("Insufficient balance!")
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()