import streamlit as st
import pandas as pd
import base64
from streamlit_option_menu import option_menu
from db_manager import valid_user
user_data = st.session_state.get('user_email', None)
user_data = valid_user(user_data)
def user_profile():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://media.licdn.com/dms/image/D5612AQERfI8EVOHq5g/article-cover_image-shrink_720_1280/0/1688683515538?e=2147483647&v=beta&t=3o1Kt9nnOqXxyuGikkRhfzzazigaVVqI4rtJl5dXCtE');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Extracting user data from session state after successful login
    
    if user_data:
        # Assuming 'user' is a tuple (id, name, email, password, regd_no, year_of_study, branch, student_type, student_image)
        name=user_data[1]
        mail=user_data[2]
        regd_no=user_data[3]
        branch=user_data[4]
        student_type=user_data[5]
        course=user_data[6]
        college_name=user_data[7]
        student_image=user_data[8]
        if isinstance(student_image, bytes):
            # Encode the binary image to base64
            image_data = base64.b64encode(student_image).decode()
            image_link = f"data:image/png;base64,{image_data}"
        elif isinstance(student_image, str) and student_image:  # In case it's a file path or URL
            try:
                # Open the image as binary if it's a valid file path
                with open(student_image, "rb") as img_file:
                    image_data = base64.b64encode(img_file.read()).decode()
                    image_link = f"data:image/png;base64,{image_data}"
            except FileNotFoundError:
                # Default image in case file is not found
                image_link = "https://cdn-icons-png.flaticon.com/512/4042/4042356.png"
        else:
            # Default image if no image data is available
            image_link = "https://cdn-icons-png.flaticon.com/512/4042/4042356.png"

        # CSS Styling
        profile_css = """
            <style>
                .profile-container {
                    background-color: #9dd3fa;
                    padding: 40px;
                    border-radius: 30px;
                    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
                    max-width: 500px;
                    margin: auto;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                .profile-image {
                    margin-bottom: 20px;
                }
                .profile-image img {
                    border-radius: 50%;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.8);
                    max-width: 250px;
                    max-height: 250px;
                }
                .profile-details {
                    margin-top: 20px;
                }
                .profile-header {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 15px;
                    color: maroon;
                }
                .profile-item {
                    font-size: 16px;
                    margin-bottom: 10px;
                    color: #333;
                }
                .profile-item strong {
                    color: red; /* Label color */
                }
            </style>
            """

            # HTML Structure
        profile_html = f"""
        <div class="profile-container">
            <div class="profile-image">
                <img src="{image_link}" alt="User Image">
            </div>
            <div class="profile-details">
                <div class="profile-item"><strong>Name:</strong> {name}</div>
                <div class="profile-item"><strong>Registration Number:</strong> {regd_no}</div>
                <div class="profile-item"><strong>Branch:</strong> {branch}</div>
                <div class="profile-item"><strong>Student Type:</strong> {student_type}</div>
                <div class="profile-item"><strong>Course:</strong> {course}</div>
                <div class="profile-item"><strong>College Name:</strong> {college_name}</div>
                <div class="profile-item"><strong>Email:</strong> {mail}</div>
            </div>
        </div>
        """


        # Display styled content
        st.markdown(profile_css + profile_html, unsafe_allow_html=True)
    else:
        st.error("User not logged in!")

def user_home_page():
    # Navigation menu for user dashboard
    with st.sidebar:
        #write Hello and name at the top of the sidebar at center with wave emoji
        st.markdown('<h1 style="text-align: center;">Hello, '+user_data[1]+'! 👋</h1>', unsafe_allow_html=True)
        selected_tab = option_menu(
            menu_title=None,
            options=["Student Profile",'Logout'],
            icons=['person-circle','unlock-fill'], menu_icon="cast", default_index=0,
        styles={
        "nav-link-selected": {"background-color": "#fcc7fc", "color": "black", "border-radius": "5px"},
        }
        )
    if selected_tab == "Student Profile":
        user_profile()
    elif selected_tab=='Logout':
        # Logout functionality
        st.session_state.clear()  # Clear session state to "log out"
        st.experimental_rerun()