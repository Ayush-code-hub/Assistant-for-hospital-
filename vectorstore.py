# vectorstore.py
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from data import RAW_KNOWLEDGE_BASE

def init_vectorstore():
    # Downloads and loads the embedding model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    docs = [
        Document(
            page_content=f"{item['title']}: {item['content']}",
            metadata={"id": item["id"], "access_level": item["access_level"], "title": item["title"]}
        ) for item in RAW_KNOWLEDGE_BASE
    ]
    
    return FAISS.from_documents(docs, embeddings)

def get_relevant_documents(vectorstore, query, k=2):
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)