# llm_engine.py
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

def get_llm(temperature=0.7):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from .env file")
    
    # Using Groq's stable, currently supported model
    return ChatGroq(api_key=api_key, model_name="openai/gpt-oss-20b", temperature=temperature)

def get_generic_response(query):
    llm = get_llm(temperature=0.7)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a general medical AI. Answer using standard global knowledge."),
        ("human", "{question}")
    ])
    chain = prompt | llm
    return chain.invoke({"question": query}).content

def get_rag_response(query, docs, user_info):
    if not docs:
        return "⚠️ **No specific Supra Hospital Protocol found.** Consult department senior."
    
    # Enforce RBAC checks
    for doc in docs:
        if doc.metadata.get("access_level") == "CONFIDENTIAL" and user_info["level"] != "CONFIDENTIAL":
            return f"<div class='alert-denied'><strong>⛔ ACCESS DENIED</strong><br>Your role ({user_info['role']}) lacks clearance for this restricted file. Incident Logged.</div>"

    context = "\n".join([d.page_content for d in docs])
    
    llm = get_llm(temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are the Supra Hospital internal AI. You MUST base your answer strictly on the Context. Do not include external standard medical advice if it contradicts the Context. Be concise."),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])
    chain = prompt | llm
    return chain.invoke({"context": context, "question": query}).content