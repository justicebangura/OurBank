import streamlit as st
from PIL import Image

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
    #st.header("Watch Our Introductory Video")
    #st.video("https://youtu.be/_k9mhRBI2cY?si=7W2DUrUU_A6ZPWlx")  # Embed video with Streamlit

    # Displaying the main image
    crypto_image = Image.open("./Images/babydov.jpg")  # Use a relevant image
    st.image(crypto_image, caption="Your Trusted Crypto Banking Partner", use_column_width=True)

    # Overview of Services
    st.header("Our Services")
    st.write(
        """
        We provide a range of services to meet your crypto banking needs, including:
        
        - **Secure Storage**: We ensure your digital assets are protected with top-notch encryption and multi-factor authentication.
        - **Easy Transactions**: Our platform makes sending funds and managing transactions effortless.
        - **Multi-Currency Support**: Handle multiple cryptocurrencies in one convenient place.
        - **Real-Time Conversion**: Convert between digital assets and fiat currencies with ease.
        """
    )

    # Call-to-Action with Button
    st.header("Get Started with OurBank")
    st.write(
        """
        Ready to join? Get started with OurBank today. 
        Whether you're a crypto enthusiast or just starting, we have the tools to help you succeed.
        """
    )
    if st.button("Open an Account"):
        st.write("Thank you for your interest! Please visit our sign-up page to get started.")  # Call-to-action feedback
