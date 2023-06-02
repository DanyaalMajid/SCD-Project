from langchain.agents import initialize_agent
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool

import streamlit as st
from streamlit_chat import message

if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []


# Define function to get user input text
def get_text():
    """
    Get the user input text.

    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], key="input",
                               placeholder="Your AI assistant here! Ask me anything ...",
                               label_visibility='hidden')
    return input_text


# Define function to start a new chat
def new_chat():
    """
    Clears session state and starts a new chat.
    """
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []


def chatbot_ui(openai_key, google_search_key, google_cse_key):
    st.title('Chatbot UI')

    # Display chatbot interface here using Streamlit components
    # You can use st.text_area, st.text_input, st.button, etc.
    # Example: Chatbot input and output
    user_input = st.text_input('User Input')
    st.write('Bot Response:', 'Hello! I am a chatbot.')


def main():
    st.set_page_config(layout='wide')

    # Display sidebar
    with st.sidebar:
        st.title('API Keys')

        st.text_input('OpenAI API Key:', key="openai_key")
        st.text_input('Google Search API Key:', key="google_search_key")
        st.text_input('Google CSE API Key:', key="google_cse_key")

    st.write('API Keys:', st.session_state)
    chatbot_ui(st.session_state["openai_key"],
               st.session_state["google_search_key"], st.session_state["google_cse_key"])


if __name__ == '__main__':
    main()
