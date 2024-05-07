<<<<<<< Updated upstream
=======
import streamlit as st
import pandas as pd
import seaborn as sns
import utils
import matplotlib.pyplot as plt

def show():
    st.title("Account Details")
    st.write("View your account information.")

    # Fetch account data from the backend and handle possible exceptions
    try:
        accounts = utils.get_accounts()  # Fetch account data
        if not accounts:
            st.warning("No accounts available. Please check back later.")
            return
    except Exception as e:
        st.error(f"Error fetching accounts: {e}")
        return

    # Provide a selection box for available accounts
    selected_account_name = st.selectbox("Select an account", [acc['name'] for acc in accounts])
    
    # Find the selected account in the accounts list
    try:
        account = next(acc for acc in accounts if acc['name'] == selected_account_name)
    except StopIteration:
        st.warning("The selected account could not be found.")
        return

    # Display account information
    st.write(f"Account: {account['name']}")
    st.write(f"Balance: {account['balance']}")

    # Create a new Matplotlib figure for the bar chart
    fig, ax = plt.subplots()  # Create a new figure and axis

    # Create mock data for demonstration
    activity = pd.DataFrame({
        "Type": ["Deposit", "Withdrawal", "Deposit"],
        "Amount": [2000, 100, 3000],
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"]
    })

    # Create the bar plot using Seaborn with Matplotlib's axis
    sns.barplot(x="Date", y="Amount", hue="Type", data=activity, ax=ax)

    # Display the bar chart
    st.pyplot(fig)  # Pass the figure to st.pyplot()
>>>>>>> Stashed changes
