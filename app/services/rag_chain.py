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
    index_file = os.path.join(index_path, "index.faiss")

    if os.path.exists(index_file):
        return FAISS.load_local(
            index_path,
            get_embedding_model(),
            allow_dangerous_deserialization=True
        )

    docs = load_and_split_documents("data/documents/Santosh-Tiwari-cv.pdf")
    vectorstore = FAISS.from_documents(docs, get_embedding_model())
    vectorstore.save_local(index_path)
    return vectorstore

def get_rag_chain():
    llm = ChatGoogleGenerativeAI(
       model="gemini-2.0-flash",
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0,
    )
    vectorstore = get_vectorstore()
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )