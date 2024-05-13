import streamlit as st
from backend.banking_account import open_new_account

# Function to display the home page
def show():
    # Title and Introduction
    st.title("Welcome to OurBank")
    st.write(
        """
        At OurBank, we are committed to providing innovative crypto banking solutions. 
        Our goal is to offer a seamless and secure experience as you manage your digital assets.
        """
    )

    # Embed YouTube Video
    st.video("./Images/homevid.mp4", format='video/mp4', start_time=0)

    # Call-to-Action with Button
    st.header("Get Started with OurBank")
    st.write(
        """
        Ready to join? Get started with OurBank today. 
        Whether you're a crypto enthusiast or just starting, we have the tools to help you succeed.
        """
    )

# Render the home page
show()

