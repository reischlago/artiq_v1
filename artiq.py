import streamlit as st
import login
import register_artist
import register_gallery

st.set_page_config(page_title="Artiq", layout="centered")

# Sidebar navigation
st.sidebar.title("Artiq Navigation")
selected = st.sidebar.radio(
    "Go to",
    ["Login", "Register Artist", "Register Gallery"]
)

# Routing
if selected == "Login":
    login.main()
elif selected == "Register Artist":
    register_artist.main()
elif selected == "Register Gallery":
    register_gallery.main()
