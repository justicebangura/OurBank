import streamlit as st
import pages.home as home
import pages.account as account
import pages.transactions as transactions
import pages.about as about
import base64
from PIL import Image

# Function to load and display the logo in the sidebar
def display_logo_in_sidebar(img_path):
    with open(img_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode("utf-8")
    
    # Custom HTML for embedding the logo in the sidebar
    logo_html = f"""
    <div style="text-align: center; padding: 10px;">
        <img 
            src="data:image/png;base64,{img_base64}" 
            alt="Logo" 
            style="width: 200px; height: 200px; border-radius: 50%;"
        />
    </div>
    """
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# Display the logo in the sidebar
display_logo_in_sidebar("../Images/transparent1.png")  # Path to the logo image

    # Navigation and content for authenticated users
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Select a Page", ("Home", "Account", "Transactions","About"))
    
if navigation == "Home":
    import pages.home as home
    home.show()
elif navigation == "Account":
    import pages.account as account
    account.show()
elif navigation == "Transactions":
    import pages.transactions as transactions
    transactions.show
elif navigation == "About":
    import pages.about as about
    about.show



