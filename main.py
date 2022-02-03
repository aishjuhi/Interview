# This is a sample Python script.
import streamlit as st
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from src.file_upload.load_data import LoadData
from src.login_flow.login_page import LoginPage


def start_flow():
    st.set_page_config(page_title='Energy Consumption Portal', page_icon=":rainbow:", layout='wide',
                       initial_sidebar_state='auto')
    login_impl = LoginPage()
    BooleanLogin = login_impl.start_login_container()
    if (BooleanLogin == True):
        st.write("Welcome admin,")
        data = LoadData()
        data.file_upload()

if __name__ == '__main__':
    start_flow()


