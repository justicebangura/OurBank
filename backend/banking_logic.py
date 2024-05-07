#import streamlit as st

# Mock user database (in a real application, you would use a proper database)
#USER_DATABASE = {
   # "user1": {"password": "password1", "balance": 1000},
    #"user2": {"password": "password2", "balance": 2000}
#}

#def authenticate_user(username, password):
   # if username in USER_DATABASE:
    #    if USER_DATABASE[username]["password"] == password:
     #       return True
   # return False

#def display_account_balance(username):
   # st.write(f"Account Balance for {username}: ${USER_DATABASE[username]['balance']}")

#def make_transaction(username, amount):
    #USER_DATABASE[username]["balance"] += amount

#def main():
    #st.title("OUR BANK")

    #username = st.text_input("Username")
    #password = st.text_input("Password", type="password")

    #if st.button("Login"):
        #if authenticate_user(username, password):
            #st.success("Login successful!")
            #display_account_balance(username)

            # Transaction options
            #st.header("Make a Transaction")
            #transaction_type = st.radio("Transaction Type", ("Deposit", "Withdraw"))
            #amount = st.number_input("Amount")

           # if st.button("Submit"):
                #if transaction_type == "Deposit":
                    #make_transaction(username, amount)
                   # st.success(f"Deposit of ${amount} successful!")
                   # display_account_balance(username)
               # elif transaction_type == "Withdraw":
                    #if amount <= USER_DATABASE[username]["balance"]:
                       # make_transaction(username, -amount)
                       # st.success(f"Withdrawal of ${amount} successful!")
                       # display_account_balance(username)
                   # else:
                      #  st.error("Insufficient balance!")
        #else:
            #st.error("Invalid username or password. Please try again.")

#if __name__ == "__main__":
    #main()
import streamlit as st

def main():
    st.title("OurBank")

    # Add tabs for different functionalities
    tabs = ["Home", "Accounts", "Deposit", "Withdraw"]
    choice = st.sidebar.selectbox("Select Option", tabs)

    if choice == "Home":
        home()
    elif choice == "Accounts":
        accounts()
    elif choice == "Deposit":
        deposit()
    elif choice == "Withdraw":
        withdraw()

def home():
    st.write("Welcome to our banking app!")

def accounts():
    st.write("View accounts here.")

def deposit():
    st.header("Deposit")
    account_number = st.text_input("Enter Account Number:")
    amount = st.number_input("Enter Amount to Deposit:", min_value=0.01)
    if st.button("Deposit"):
        # Logic to perform deposit
        st.success(f"Successfully deposited ${amount} into account {account_number}.")

def withdraw():
    st.header("Withdraw")
    account_number = st.text_input("Enter Account Number:")
    amount = st.number_input("Enter Amount to Withdraw:", min_value=0.01)
    if st.button("Withdraw"):
        # Logic to perform withdrawal
        st.success(f"Successfully withdrew ${amount} from account {account_number}.")

if __name__ == "__main__":
    main()
    