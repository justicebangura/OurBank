<<<<<<< Updated upstream
=======
import streamlit as st
import utils
from PIL import Image
import matplotlib.pyplot as plt


# Main page content
def show():
    st.title("Welcome to OurBank!")
    st.write("Your trusted partner in crypto banking.")

    st.subheader("Account Overview")

    # Fetching account data from backend and handle potential exceptions
    try:
        accounts = utils.get_accounts()
        if not accounts:
            st.warning("No accounts found. Please check back later.")
            return
    except Exception as e:
        st.error(f"Error fetching accounts: {e}")
        return

    # Create a new Matplotlib figure for the pie chart
    fig, ax = plt.subplots()  # Create a new figure and axes
    
    # Create the pie chart with account balances
    labels = [account['name'] for account in accounts]
    balances = [account['balance'] for account in accounts]
    
    ax.pie(balances, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Ensures the pie chart is circular

    # Display the pie chart
    st.pyplot(fig)  # Pass the figure to st.pyplot()
>>>>>>> Stashed changes
