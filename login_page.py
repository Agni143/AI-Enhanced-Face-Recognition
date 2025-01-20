import streamlit as st
import sqlite3
import face_recognition as frg
import io

def fetch_registered_image(email):
    """
    Fetch the registered image for the given email from the database.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT student_image FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def login_page():
    # Center the login form using Streamlit form layout
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.shutterstock.com/image-photo/child-boy-using-tablet-looking-600nw-2225757071.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.5);
        background-blend-mode: overlay;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    col1,col2,col3=st.columns([3,8,3])
    with col2.form(key="login_form"):
        # Title
        st.title("Sign In") 

        # Email and Password inputs
        email = st.text_input("Email")
        uploaded_image=st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        
        # Submit button inside the form
        login_button = st.form_submit_button("Login",type="primary")

        # Handling form submission
        if login_button:
            if not email or not uploaded_image:
                st.error("Both email and image are required for login.")
                return

            # Fetch the registered image for the email
            registered_image_data = fetch_registered_image(email)
            if not registered_image_data:
                st.error("Email not found. Please register first.")
                return

            # Validate uploaded image against registered image
            try:
                # Convert database binary image into a file-like object
                registered_image_stream = io.BytesIO(registered_image_data)
                registered_image = frg.load_image_file(registered_image_stream)

                # Convert uploaded image into a file-like object
                uploaded_image_stream = io.BytesIO(uploaded_image.read())
                uploaded_image_data = frg.load_image_file(uploaded_image_stream)

                # Generate face encodings for both images
                registered_encoding = frg.face_encodings(registered_image)[0]
                uploaded_encoding = frg.face_encodings(uploaded_image_data)[0]

                # Compare the face encodings
                is_match = frg.compare_faces([registered_encoding], uploaded_encoding, tolerance=0.5)

                if is_match[0]:
                    st.success("Login successful!")
                    # Store session information or redirect
                    st.session_state["page"] = "user_home"
                    st.session_state["user_email"] = email
                    st.session_state["user_tab"] = "Loan Page"
                    st.session_state["logged_in"] = True
                    st.experimental_rerun()

                else:
                    st.error("Face mismatch. Please try again.")
            except IndexError:
                st.error("Face not detected in one or both images. Please use a clear image.")
