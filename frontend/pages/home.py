import streamlit as st
import utils
from PIL import Image
import matplotlib.pyplot as plt


# Main page content
def show():

    st.title("Welcome to OurBank!")
    st.write("Your trusted partner in crypto banking.")

    st.subheader("Account Overview")
    accounts = utils.get_accounts()  # Fetching account data from backend

    # Use a pie chart to visualize the account balances
    labels = [account['name'] for account in accounts]
    balances = [account['balance'] for account in accounts]

    plt.pie(balances, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    st.pyplot()  # Display the chart