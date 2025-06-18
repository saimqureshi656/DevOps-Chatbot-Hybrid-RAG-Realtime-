from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from tools.tavily_search import tavily_web_search


load_dotenv()

llm = ChatGroq(
    groq_api_key = os.getenv('GROQ_API_KEY'),
    model_name = 'llama3-70b-8192')

embedding_model = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
vector_store=FAISS.load_local("devops_vector_db", embedding_model,allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever(search_kwargs={"k": 4})

# Prompt template
prompt_template = PromptTemplate.from_template("""
You are a senior DevOps engineer.

Answer the question below in a clear, structured, and professional manner. Use the following context:
- **Internal Documentation**: Based on DevOps PDFs
- **Web Search Results**: Fresh insights from the internet

Question: {question}

📚 Internal Docs:
{internal_context}

🌐 Web Results:
{web_context}

Be accurate, provide steps or examples if needed, and end your answer politely.
""")

def ask_devops_bot(user_query):
    web_context = tavily_web_search(user_query)
    internal_docs = retriever.get_relevant_documents(user_query)
    internal_context = "\n\n".join([doc.page_content for doc in internal_docs])
    full_prompt = prompt_template.format(
        question=user_query,
        internal_context=internal_context,
        web_context=web_context
    )
    
    response = llm.invoke([HumanMessage(content=full_prompt)])
    return response.content.strip()
