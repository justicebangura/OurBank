import streamlit as st
import frontend.pages.home as home
import frontend.pages.account as account
import frontend.pages.features as features
import frontend.pages.about as about
import base64


# Function to load and display the logo in the sidebar
def display_logo_in_sidebar(img_path):
    with open(img_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode("utf-8")
    
    # Custom HTML for embedding the logo in the sidebar
    logo_html = f"""
    <div style="text-align: center; padding: 20px;">
        <img 
            src="data:image/png;base64,{img_base64}" 
            alt="Logo" 
            style="width: 250px; height: 250px; border-radius: 50%;"
        />
    </div>
    """
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# Display the logo in the sidebar
display_logo_in_sidebar("Images/transparent1.png")  # Path to the logo image

    # Navigation and content for authenticated users
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Select a Page", ("Home", "Account", "Features","About"))
    
if navigation == "Home":
    import frontend.pages.home as home
    home.show()
elif navigation == "Account":
    import frontend.pages.account as account
    account.show()
elif navigation == "Features":
    import frontend.pages.features as features
    features.show()
elif navigation == "About":
    import frontend.pages.about as about
    about.show()

