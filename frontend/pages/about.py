import streamlit as st
from PIL import Image

# Function to display the About page
def show():
    # Page Title
    st.title("About OurBank")

    # Introduction with Emphasis
    st.write(
        """
        **At OurBank, we are committed to providing exceptional crypto banking services.**
        Our goal is to combine innovation with customer satisfaction, offering cutting-edge 
        Blockchain solutions for all your financial needs.
        """
    )

    # Our Mission Statement
    st.header("Our Mission")
    st.write(
        """
        Our mission is to revolutionize the crypto banking industry by offering secure, reliable, 
        and customer-centric services. We believe in building lasting relationships with our clients 
        through transparency and trust.
        """
    )

    # Information About the Team
    st.header("Meet the Team")
    st.write(
        """
        We have a team of experienced professionals, all certified by the University of Toronto's 
        Fintech program. Our team is dedicated to helping you achieve your financial goals.
        """
    )

    # Team Member Display
    col1, col2 = st.columns(2)  # Creating two columns for a balanced layout

    with col1:
        # Displaying images of the OurBank Team
        img_justice = Image.open("./Images/Justice.png")
        small_img_justice = img_justice.resize((150, 150))  # Smaller image for the team
        st.image(small_img_justice, caption="Justice Bangura", use_column_width=False)

    with col2:
        st.write(
            """
            **Justice Bangura** is a lead Blockchain engineer and fintech expert. 
            He brings a wealth of experience in crypto technologies and is passionate about 
            creating innovative financial solutions.
            """
        )

    # Call-to-Action to Engage with the Bank
    st.header("Get in Touch")
    st.write(
        """
        We're always here to help. Whether you have questions about our services or need assistance, 
        feel free to reach out to us. Join our community to stay updated with the latest developments 
        in the crypto banking world.
        """
    )
    st.button("Contact Us", key="contact_us")  # Call-to-action button for user interaction
