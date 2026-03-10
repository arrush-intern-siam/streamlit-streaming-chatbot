import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ---------- Load Environment Variables ----------
load_dotenv()  # Loads variables from .env file

# Fetch API Key
g_key = os.getenv("g") 

#safety check
if not g_key:
    raise ValueError("API keys not found. Check your .env file.")

genai.configure(api_key=g_key)

st.title("Gemini 2.0 Streaming Assistant")

model = genai.GenerativeModel('gemini-flash-latest')

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display Chat History
for message in st.session_state.chat_session.history:
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Handle User Input
if prompt := st.chat_input("Ask Gemini 2.0 anything..."):
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        # streaming response
        response = st.session_state.chat_session.send_message(prompt, stream=True)
        
        def stream_gemini():
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        
        st.write_stream(stream_gemini)