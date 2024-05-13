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

    # Form for user input
    with st.form("create_account"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label="Create Account")

    # If the form is submitted, call the function to open a new account with provided username and password
    if submit_button:
        try:
            open_new_account(username, password)
            st.success("Account created successfully! You can now log in.")
        except ValueError as e:
            st.warning(str(e)) 

# Render the home page
show()

