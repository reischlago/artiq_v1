import streamlit as st

def main():
    st.markdown('<h1 style="text-align: center;">Artiq - Register as Gallery</h1>', unsafe_allow_html=True)

    # Step 1
    st.header("Step 1: Basic Info")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    password_again = st.text_input("Password again", type="password")
    logo = st.file_uploader("Logo")

    if st.button("Next to Step 2"):
        st.session_state.gallery_step = 2

    # Step 2
    if st.session_state.get("gallery_step") == 2:
        st.header("Step 2: Contact Info")
        country = st.text_input("Country")
        city = st.text_input("City")
        address = st.text_input("Address")
        medium = st.text_input("Art medium")
        public_email = st.text_input("Public email address")
        public_phone = st.text_input("Public phone number")
        website = st.text_input("Website URL")
        instagram = st.text_input("Instagram")

        if st.button("Next to Step 3"):
            st.session_state.gallery_step = 3

    # Step 3
    if st.session_state.get("gallery_step") == 3:
        st.header("Step 3: Bio & Portfolio")
        bio = st.text_area("Bio")
        portfolio = st.file_uploader("Portfolio", accept_multiple_files=True)

        if st.button("Register"):
            st.success("Gallery registered successfully!")
            st.session_state.gallery_step = 1
