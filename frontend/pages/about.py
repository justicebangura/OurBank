import streamlit as st
from PIL import Image

# function to display the About page
def show():
    st.title("About OurBank")
    st.write("At OurBank, our mission is to provide top-notch crypto banking with a focus on customer satisfaction and Blockchain solutions.")

    st.subheader("Our Team")
    st.write("We have a UoFT Fintech Certified team dedicated to helping you achieve your financial goals.")

    # Displaying images of the Our Bank Team 
    img = Image.open("../Images/Justice.png")
    small_img = img.resize((200, 200)) 
    st.image(small_img, caption="Justice Bangura", use_column_width=False)

    # Displaying images of the Our Bank Team 
    img = Image.open("../Images/Justice.png")
    small_img = img.resize((200, 200)) 
    st.image(small_img, caption="Justice Bangura", use_column_width=False)

    # Displaying images of the Our Bank Team 
    img = Image.open("../Images/Justice.png")
    small_img = img.resize((200, 200)) 
    st.image(small_img, caption="Justice Bangura", use_column_width=False)

    # Displaying images of the Our Bank Team 
    img = Image.open("../Images/Justice.png")
    small_img = img.resize((200, 200)) 
    st.image(small_img, caption="Justice Bangura", use_column_width=False)