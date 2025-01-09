from modules.load_config import app_conf
import streamlit as st


def creds_entered():

    if ((st.session_state["user"].strip() == app_conf()['APP_USER']) and
        (st.session_state["passwd"].strip() == app_conf()['APP_PASSWORD'])
       ):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter a password.")
        elif not st.session_state["user"]:
            st.warning("Please enter your user name.")
        else:
            st.error("Invalid Username/Password :face_with_raised_eyebrow:")    
    
    return
    
def authenticate_user():
    
    if "authenticated" not in st.session_state:
        st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", on_change=creds_entered)
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", on_change=creds_entered)
            return False