import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA



from app.utils.loader import load_and_split_documents
from app.core.config import settings

def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_vectorstore():
    index_path = "vectorstore/faiss_index"
    if os.path.exists(index_path):
        return FAISS.load_local(index_path, get_embedding_model())
    docs = load_and_split_documents("data/documents/your-doc.pdf")
    vectorstore = FAISS.from_documents(docs, get_embedding_model())
    vectorstore.save_local(index_path)
    return vectorstore

def get_rag_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0,
    )
    vectorstore = get_vectorstore()
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )