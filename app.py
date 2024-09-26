import streamlit as st
import requests

st.title("AI Therapist")

# Input field
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    response = requests.post("http://127.0.0.1:5000/api", json={"input": user_input})
    st.write(response.json())
