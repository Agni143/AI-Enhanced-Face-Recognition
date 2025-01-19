import streamlit as st
from login_page import login_page
from register_page import register_page
from db_manager import init_db
from streamlit_option_menu import option_menu
from home_page import home_page
st.write('hi')
# Initialize the database
init_db()

# Session State Initialization
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if st.session_state["page"] == "Home":
    # Horizontal navigation for non-logged-in users
    st.markdown(
        """
        <div style="text-align: center; padding: 0px; background-color: #f8a5fa; border-radius: 10px; border: 2.5px solid black; margin-bottom: 20px;">
            <p style="color: black; font-size: 40px;"><b>AI-Enhanced Face Recognition and Access Control System</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_page = option_menu(
        menu_title=None,
        options=["Home", "Login", "Register"],
        icons=["house", "box-arrow-in-right", "person-plus"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "nav-link-selected": {
                "background-color": "#ad10ab",  # Background color of the selected item
                "color": "white",
            },
            "nav-link": {
                "background-color": "#fcc7fc",  # Background color of unselected items
                "color": "black",  # Text color of unselected items
            },
        },
    )

    # Render the selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Login":
        login_page()
    elif selected_page == "Register":
        register_page()

elif st.session_state["page"] == "user_home":
    # Redirect to the user dashboard after login
    from user_home import user_home_page
    user_home_page()
