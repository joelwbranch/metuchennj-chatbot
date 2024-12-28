import pinecone_assistant
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
import configparser
import streamlit as st
import time

config = configparser.ConfigParser()
config.read("configs/config.ini")

# Initialize Pinecone assistant
pc = Pinecone(api_key=config["pinecone"]["api_key"])
assistant_name = config["pinecone"]["assistant_name"]

try:
    file_path = "data/metuchen_ordinances.pdf"
    metadata = {"city": "Metuchen", "document_type": "ordinances", "year": 2024}
    asst = pinecone_assistant.create_assistant(pc)
    resp = pinecone_assistant.upload_file(asst, file_path, metadata)
except Exception as e:
    asst = pc.assistant.Assistant(assistant_name=assistant_name)

# Define streamlit app
st.title("💬 Metuchen Ordinances Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    input = Message(role="user", content=prompt)
    with st.spinner("Thinking..."):
        resp = asst.chat(messages=[input])

    ans = resp["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": ans})
    st.chat_message("assistant").write(ans)
