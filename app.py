import streamlit as st
from streamlit_option_menu import option_menu
import json
from Home import dashboard
import pymongo
from dotenv import load_dotenv
import os
import re

load_dotenv()

from pymongo.mongo_client import MongoClient

uri = os.environ["MONGO_CONNECTION_STRING"]

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["Cosmo"]

col = db["Users"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def validate_email(email):
  """Validates the format of an email address."""
  email_regex = r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  if not re.match(email_regex, email):
    return False
  return True


def login():
    st.write("Login")
    if username := st.text_input("Email"):
        if validate_email(username):
            st.success("The email address is valid.")
        else:
            st.error("The email address is not valid.")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        document = col.find_one({"Username": username})
        if document:
            if password == document["Password"]:
                st.session_state.user = username
                st.experimental_rerun()
            else:
                st.error("Incorrect Password")
        else:
            st.error("Incorrect Email")
            
            
def register():
    st.write("Register")
    username = st.text_input("Email")
    if validate_email(username):
        st.success("The email address is valid.")
    else:
        st.error("The email address is not valid.")
    password = st.text_input("Password", type="password")
    data = {
        "Username": username,
        "Password": password
    }
    if st.button("Register"):
        col.insert_one(data)
        st.success("User created!")




def main():
    if 'user' not in st.session_state:
        st.session_state.user = None
        
    if st.session_state.user is None:
        with st.sidebar:
            selected = option_menu(None, ['Login', 'Register'])
        if selected == 'Login':
            login()
        elif selected == 'Register':
            register()
    else:
        dashboard()


main()