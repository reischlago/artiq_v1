import streamlit as st

def main():
    st.markdown('<h1 style="text-align: center;">Artiq</h1>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success(f"Welcome back, {email}!")

    st.markdown("Don't have an account yet? **Register here**")
