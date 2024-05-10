# features.py
import streamlit as st
from PIL import Image

# Load necessary images or assets
crypto_bank_image = Image.open("./Images/OurBank.png")

# Define the 'show' function for the features page
def show():
    # Title and Introduction with Images
    st.title("Welcome to OurBank")
    st.image(crypto_bank_image, caption="Your Trusted Crypto Banking Partner",  width=333)

    st.write(
        """
        OurBank offers a wide range of services to help you manage your digital assets with ease. 
        Explore our features and discover how we can make your crypto journey smooth and secure.
        """
    )

    # Features List with Columns and Icons
    st.header("Key Features")

    # Secure Storage
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./Images/secure.jpg", width=64)  # Secure storage icon
    with col2:
        st.subheader("Secure Storage")
        st.write(
            """
            We use advanced encryption and multi-factor authentication to ensure the safety of your assets. 
            Your cryptocurrencies are stored securely, and only you have access.
            """
        )

    # Easy Transactions
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./Images/easy.jpg", width=64)  # Easy transactions icon
    with col2:
        st.subheader("Easy Transactions")
        st.write(
            """
            Conduct transactions effortlessly. Whether you're sending funds, investing, or purchasing goods, 
            our platform makes it easy to manage your transactions.
            """
        )

    # Multi-Currency Support
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./Images/multi.png", width=64)  # Multi-currency icon
    with col2:
        st.subheader("Multi-Currency Support")
        st.write(
            """
            Our Crypto Bank supports a variety of cryptocurrencies, including Bitcoin, Ethereum, Litecoin, 
            and more. Manage all your digital assets in one place.
            """
        )

    # Real-Time Conversion
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./Images/conversion.png", width=64)  # Real-time conversion icon
    with col2:
        st.subheader("Real-Time Conversion")
        st.write(
            """
            Convert your cryptocurrencies with real-time rates. Exchange between different digital assets 
            or convert to fiat currencies quickly and easily.
            """
        )

    # Comprehensive Account Management
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./Images/account.jpg", width=64)  # Account management icon
    with col2:
        st.subheader("Comprehensive Account Management")
        st.write(
            """
            Manage your account with complete control. Track balances and view transaction history.
            """
        )

    # Call-to-Action with Button
    st.header("Get Started")
    st.write(
        """
        Join us today and experience the convenience and security. 
        Whether you're a crypto enthusiast or just starting out, we have the tools you need to succeed.
        """
    )
    st.button("Open an Account", key="open_account")  # Call-to-action button

