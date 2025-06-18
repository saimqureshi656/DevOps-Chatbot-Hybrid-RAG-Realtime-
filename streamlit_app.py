
import streamlit as st
import requests

st.title("DevOps Assistant")
st.markdown("Ask anything related to DevOps. Answers come from internal docs + latest web search (Hybrid RAG & Realtime).")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

query = st.chat_input("Ask a DevOps question...")
if query:
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Asking DevOps Assistant..."):
        res = requests.post("http://localhost:8000/chat", json={"question": query})
        answer = res.json()["response"]

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

