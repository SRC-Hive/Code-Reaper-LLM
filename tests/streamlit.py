import streamlit as st
from test import get_bot_response

# Set up the page configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Title and Description
st.title("🤖 Chatbot Interface")
st.markdown("Feel free to ask any questions.")

# Initialize the conversation in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Function to handle input and response
def handle_input():
    user_input = st.session_state.input_text
    if user_input:
        response = get_bot_response(user_input)
        st.session_state.conversation.append({"role": "user", "message": user_input})
        st.session_state.conversation.append({"role": "bot", "message": response})
        st.session_state.input_text = ""  # Clear input field

# Placeholder for the conversation
conversation_placeholder = st.container()

# Text input box at the bottom
with st.container():
    user_input = st.text_input("Type your message here...", key="input_text", on_change=handle_input)

# Function to render the chat bubbles
def render_message(role, message):
    if role == "user":
        st.markdown(f"""
        <div style="background-color: #000000; color: #FFFFFF; padding: 10px; border-radius: 10px; margin-bottom: 10px; text-align: left; max-width: 60%; word-wrap: break-word;">
            <strong>You:</strong> {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; color: #000000; padding: 10px; border-radius: 10px; margin-bottom: 10px; text-align: left; max-width: 60%; margin-left: auto; word-wrap: break-word;">
            <strong>Bot:</strong> {message}
        </div>
        """, unsafe_allow_html=True)

# Display the conversation history in the placeholder
with conversation_placeholder:
    for chat in st.session_state.conversation:
        render_message(chat["role"], chat["message"])

# Option to clear the conversation history
if st.button("Clear Conversation"):
    st.session_state.conversation = []
