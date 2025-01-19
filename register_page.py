import streamlit as st
import re
from db_manager import register_user

def register_page():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.shutterstock.com/image-photo/businesswoman-wearing-casual-wear-touching-260nw-2255229609.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.4); /* Add a semi-transparent overlay */
        background-blend-mode: overlay; /* Blend the image with the overlay */

    }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Center the registration form container using Streamlit form layout
    with st.form(key="register_form"):
        # Title
        st.title("Sign Up")
        # Form Fields
        col1, col2 = st.columns(2)
        name = col1.text_input("Name of Student")
        email = col2.text_input("Enter College Email")
        regd_no = col1.text_input("Registration Number")
        branch = col2.selectbox("Branch of Study", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT", "AIDS", "BIO-TECH", "CHEMICAL", "ARCHITECTURE"])
        student_type = col1.selectbox("Student Type", ["Day Scholar", "Hosteller"])
        course=col2.selectbox("Course of Study",["B.Tech","M.Tech","PhD","MBA","MCA","B.Sc","M.Sc","B.A","M.A","B.Com","M.Com"])
        college_name=col1.text_input("Enter College Name")
        student_image = col2.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        col1, col2 = st.columns(2)
        # Submit Button inside the form
        register_button = st.form_submit_button("Register",type='primary')

        # Handling form submission
        if register_button:
            # Validate email using regex
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                st.error("Invalid Email!")
            else:
                if register_user(name, email, regd_no, branch, student_type, course, college_name, student_image):
                    st.success("Registration Successful!")
                else:
                    st.error("Email already exists!")
