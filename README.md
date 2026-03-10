# Chatbot UI with Streamlit & Chainlit (Gemini API)

This project demonstrates how to build **LLM-powered chatbots using modern Python UI frameworks**.  
The chatbot is powered by **Google Gemini models** and implemented using both **Streamlit** and **Chainlit**, along with **real-time response streaming**.

The goal of this project is to explore different approaches to building conversational AI interfaces and understand how **streaming responses improve the user experience**.

---

# Project Overview

The project consists of **three tasks**, each demonstrating a different way of building chatbot interfaces.

| Task | Description | Script |
|-----|-------------|-------|
| Task 1 | Build a basic chatbot UI using Streamlit | `streamlit_app.py` |
| Task 2 | Build a similar chatbot interface using Chainlit | `chainlit_app.py` |
| Task 3 | Implement real-time response streaming | `streamlit_streaming_app.py` |

All applications use the **Gemini Flash model** to generate responses.

---

# Project Structure
day-9/

│

├── streamlit_app.py

├── chainlit_app.py

├── streamlit_streaming_app.py

└── README.md

---

# Features

- Conversational chatbot interface  
- Chat history management  
- Google Gemini API integration  
- Multiple UI frameworks  
- Real-time response streaming  
- Environment variable based API key management  

---

# Technologies Used

- Python  
- Streamlit  
- Chainlit  
- Google Generative AI (Gemini API)  
- python-dotenv  

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/chatbot-streamlit-chainlit.git
cd chatbot-streamlit-chainlit
```

## Install Dependencies
```bash
pip install streamlit chainlit google-generativeai python-dotenv
```

## Configure Environment Variables
Create a .env file in the project root:
`g=YOUR_GEMINI_API_KEY`

---

# Running the Applications

## Run the Streamlit Chatbot
Basic chatbot UI built with Streamlit.

```bash
streamlit run streamlit_app.py
```

**Features**
- Simple conversational interface
- Chat history using st.session_state
- Gemini response generation

## Run the Chainlit Chatbot

Chatbot built using Chainlit framework.
```bash
chainlit run chainlit_app.py
```

**Features**
- Built-in chat interface
- Session-based conversation tracking
- Gemini model integration

## Run the Streaming Chatbot
Streamlit chatbot with real-time response streaming.
```bash
streamlit run streamlit_streaming_app.py
```

**Features**
- Streaming responses from Gemini
- Token-by-token output rendering
- Improved conversational experience

---

# How the Chatbot Works
1. The user sends a message via the UI.
2. The message is appended to the conversation history.
3. The conversation history is sent to the Gemini model.
5. Gemini generates a response.
6. The response is displayed in the chat interface.

## For the Streaming Version
1. The model response is streamed in chunks.
2. Each chunk is displayed incrementally in the UI.

---