import streamlit as st
from login_page import login_page
def home_page():
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area with transparency */
        .main {
            background-image: url('https://cdn.impossibleimages.ai/wp-content/uploads/2023/04/25130031/AI-Background-Image-Generator-How-It-Works-and-Why-You-Need-It.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.3); /* Add a semi-transparent overlay */
            background-blend-mode: overlay; /* Blend the image with the overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    #add image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdni.iconscout.com/illustration/premium/thumb/mobile-face-recognition-illustration-download-in-svg-png-gif-file-formats--image-identity-verification-biometric-technology-and-protection-pack-science-illustrations-4708010.png?f=webp" style="max-width: 100%;">
        </div>
        """,
        unsafe_allow_html=True
    )

