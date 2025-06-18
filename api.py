from fastapi import FastAPI
from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage

from app import llm, retriever, prompt_template
from tools.tavily_search import tavily_web_search

app = FastAPI()

class Query(BaseModel):
    question: str

# ✅ Single memory instance for the whole session
memory = ConversationBufferMemory(return_messages=True)

@app.get("/")
def read_root():
    return {"message": "DevOps Chatbot is live!"}

@app.post("/chat")
def chat_endpoint(request: Query):
    question = request.question

    internal_docs = retriever.get_relevant_documents(question)
    internal_context = "\n\n".join([doc.page_content for doc in internal_docs])
    web_context = tavily_web_search(question)

    full_prompt = prompt_template.format(
        question=question,
        internal_context=internal_context,
        web_context=web_context
    )

    # ✅ Add memory chat history to LLM input
    response = llm.invoke(memory.chat_memory.messages + [HumanMessage(content=full_prompt)])

    # ✅ Update memory with new interaction
    memory.chat_memory.add_user_message(question)
    memory.chat_memory.add_ai_message(response.content)

    return {"response": response.content}
