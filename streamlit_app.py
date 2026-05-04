# streamlit_app.py
import streamlit as st

st.title("AI Chatbot")
st.write("Welcome to my Streamlit AI Chatbot app!")

# Simple chatbot input/output
user_input = st.text_input("You:", "")
if user_input:
    st.write("Bot:", f"You said: {user_input}")
