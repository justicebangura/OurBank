import streamlit as st
import utils
import pandas as pd
import seaborn as sns

def show():
    st.title("Account Details")
    st.write("View your account information.")

    accounts = utils.get_accounts()  # Fetch account data from backend

    selected_account = st.selectbox("Select an account", [acc['name'] for acc in accounts])
    account = next(acc for acc in accounts if acc['name'] == selected_account)

    st.write(f"Account: {account['name']}")
    st.write(f"Balance: {account['balance']}")

    # Show a bar chart of account activity (mock data for demonstration)
    activity = pd.DataFrame({
        "Type": ["Deposit", "Withdrawal", "Deposit"],
        "Amount": [2000, 100, 3000],
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"]
    })

    sns.barplot(x="Date", y="Amount", hue="Type", data=activity)
    st.pyplot()  # Display the bar chart
