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
        # Displaying images of Justice Bangura
        img_justice = Image.open("./Images/Justice.png")
        small_img_justice = img_justice.resize((150, 150))  # Smaller image for the team
        st.image(small_img_justice, caption="Justice Bangura", use_column_width=False)

        # Information about Justice Bangura
        st.write(
            """
            **Justice Bangura** is a lead Blockchain engineer and fintech expert. 
            He brings a wealth of experience in crypto technologies and is passionate about 
            creating innovative financial solutions.
            """
        )

        # Displaying images of Hyun Bin Shin
        img_hyunbin = Image.open("./Images/Bin.JPG")
        small_img_hyunbin = img_hyunbin.resize((150, 150))  # Smaller image for the team
        st.image(small_img_hyunbin, caption="Hyun Bin Shin", use_column_width=False)

        # Information about Hyun Bin Shin
        st.write(
            """
            **Hyun Bin Shin** is a smart contract developer responsible for ensuring 
            the functionality and security of OurBank's smart contracts. He leverages 
            blockchain technology to create robust and efficient financial solutions.
            """
        )

    with col2:
        # Displaying images of Katie Nieuwhof
        img_katie = Image.open("./Images/Katie.JPG")
        small_img_katie = img_katie.resize((150, 150))  # Smaller image for the team
        st.image(small_img_katie, caption="Katie Nieuwhof", use_column_width=False)

        # Information about Katie Nieuwhof
        st.write(
            """
            **Katie Nieuwhof** is a lead developer of the Crypto Wallet. 
            She specializes in the development of secure and user-friendly 
            solutions for managing digital assets.
            """
        )

        # Displaying images of Sahib Gandhi
        img_hyunbin = Image.open("./Images/Sahib.JPG")
        small_img_hyunbin = img_hyunbin.resize((150, 150))  # Smaller image for the team
        st.image(small_img_hyunbin, caption="Hyun Bin Shin", use_column_width=False)

        # Information about Hyun Bin Shin
        st.write(
            """
            **Sahib Gandhi** Is in charge of the back end logic of the applications and ensuring everything is 
            running smoothly. His primary responsibility is to design and implement Streamlit functions 
            that visualize data, enable user interaction, and deliver insights efficiently. Sahib leveraged
            Streamlit's intuitive APls to develop engaging and user-friendly applications for data analysis, 
            machine learning, visualization, and more.
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
        if st.button("Check out our GitHub Repository", key="github_repo"):
            st.write("Check out our GitHub repository for the project:")
            st.markdown("[OurBank GitHub Repository](https://github.com/justicebangura/OurBank.git)")  # Call-to-action feedback

# Display the About page
show()
