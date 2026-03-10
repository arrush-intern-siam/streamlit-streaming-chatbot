import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ---------- Load Environment Variables ----------
load_dotenv()  # Loads variables from .env file

# Fetch API Key
g_key = os.getenv("g") 

#safety check
if not g_key:
    raise ValueError("API keys not found. Check your .env file.")

# Configure the API key
genai.configure(api_key=g_key)

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash') 

st.title("My Gemini Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"])

# React to user input
if prompt := st.chat_input("What is up?"):
    
    # 1. Save the user's message to our history
    st.session_state.messages.append({"role": "user", "parts": prompt})
    
    # 2. Display the user's message right away
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Generate and display the model's response
    with st.chat_message("model"):
        response = model.generate_content(st.session_state.messages)
        st.markdown(response.text)
        
    # 4. Save the model's response to our history
    st.session_state.messages.append({"role": "model", "parts": response.text})