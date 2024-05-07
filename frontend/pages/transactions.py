import streamlit as st
import utils

def show():
    st.title("Transactions")
    st.write("View and manage your transactions.")

    # Fetching transaction data from the backend
    transactions = utils.get_transactions()

    # Display transactions in a table with sorting
    st.dataframe(transactions)

    st.subheader("Add a New Transaction")
    with st.form("transaction_form"):
        description = st.text_input("Description")
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        transaction_type = st.selectbox("Type", ["Deposit", "Withdrawal"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            # In a real app, you would send this data to the backend to create a new transaction
            st.success("Transaction added!")
