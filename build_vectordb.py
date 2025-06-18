from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

pdf_folder = "C:/Users/WAJIZ.PK/Desktop/Python_projects/DevOps_realtime/data"
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

all_docs = []
for file in pdf_files:
    loader = PyPDFLoader(os.path.join(pdf_folder, file))
    docs = loader.load()
    all_docs.extend(docs)


splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_documents(all_docs)


embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(chunks, embedding_model)
vector_store.save_local("devops_vector_db") 

