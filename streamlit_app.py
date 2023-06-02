import streamlit as st
from streamlit_chat import message

from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent

st.title("MemoryBot With Google!")

openai_key = st.secrets["openai_key"]
google_api = st.secrets["google_api"]
google_cse = st.secrets["google_cse"]

with st.sidebar:
    st.header("Settings")


container = st.container()

input_text = container.text_input(
    "You: ", placeholder="Ask Me Something!", key="input")


if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True)

memory = st.session_state['memory']

search = GoogleSearchAPIWrapper(
    google_api_key=google_api, google_cse_id=google_cse)

tools = Tool(
    name="Search",
    description="Search Google for recent results.",
    func=search.run
)

llm = ChatOpenAI(temperature=0, openai_api_key=openai_key,
                 model_name="gpt-3.5-turbo")

agent_chain = initialize_agent(
    [tools],
    llm,
    agent="chat-conversational-react-description",
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)

if 'generated' not in st.session_state:
    st.session_state['generated'] = [
        "Hello! I am an AI Chatbot with memory and internet access."]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Type Something....."]

user_input = input_text

if user_input:
    output = agent_chain.run(input=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
