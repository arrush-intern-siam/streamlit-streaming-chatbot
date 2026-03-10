import chainlit as cl
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

@cl.on_chat_start
def start_chat():
    # cl.user_session is Chainlit's equivalent to st.session_state
    cl.user_session.set("messages", [])

@cl.on_message
async def main(message: cl.Message):
    # 1. Retrieve the conversation history
    messages = cl.user_session.get("messages")
    
    # 2. Add the new user message to the history
    messages.append({"role": "user", "parts": message.content})
    
    # 3. Generate the response from Gemini
    response = model.generate_content(messages)
    
    # 4. Save the model's response to the history
    messages.append({"role": "model", "parts": response.text})
    
    # 5. Send the response back to the chat UI
    await cl.Message(content=response.text).send()