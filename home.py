import streamlit as st
from app_model.login import hash_password, valid_hash
from app_model.users import add_user, get_user
from app_model.db import get_db_connection_user

g
conn = get_db_connection_user()

st.header("Home Page")
st.write("Welcome to the home page of the application")


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


tab_login, tab_register = st.tabs(["Login", "Register"])



with tab_login:
    login_name = st.text_input("Username:", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In", key="login_button"):
        user = get_user(conn, login_name)

        if user:
            user_id, username, stored_hash = user

            if username == login_name and valid_hash(login_password, stored_hash):
                st.session_state["logged_in"] = True
                st.success("You are now logged in.")
            else:
                st.error("Invalid username or password.")
        else:
            st.error("User not found.")



with tab_register:
    st.info("Registration:")
    reg_name = st.text_input("Username:", key="register_username")
    reg_password = st.text_input("Password", type="password", key="register_password")

    if st.button("Register", key="register_button"):
        if reg_name and reg_password:
            hashed_psw = hash_password(reg_password)

            try:
                add_user(conn, reg_name, hashed_psw)
                st.success("Registered successfully!")
            except Exception as e:
                st.error(f"Registration failed: {e}")
        else:
            st.error("Please fill in both fields.")
