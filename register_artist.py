import streamlit as st

def main():
    st.markdown('<h1 style="text-align: center;">Artiq - Register as Artist</h1>', unsafe_allow_html=True)

    # Step 1
    st.header("Step 1: Basic Info")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    password_again = st.text_input("Password again", type="password")
    profile_picture = st.file_uploader("Profile picture")

    if st.button("Next to Step 2"):
        st.session_state.artist_step = 2

    # Step 2
    if st.session_state.get("artist_step") == 2:
        st.header("Step 2: Contact & Bio")
        instagram = st.text_input("Instagram")
        website = st.text_input("Website URL")
        phone = st.text_input("Phone number")
        email_address = st.text_input("Email address")
        city = st.text_input("Country / City")
        bio = st.text_area("Bio")

        if st.button("Next to Step 3"):
            st.session_state.artist_step = 3

    # Step 3
    if st.session_state.get("artist_step") == 3:
        st.header("Step 3: Art Info")
        medium = st.text_input("Art medium")
        portfolio = st.file_uploader("Portfolio", accept_multiple_files=True)

        if st.button("Register"):
            st.success("Artist registered successfully!")
            st.session_state.artist_step = 1
