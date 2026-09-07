# app.py
import streamlit as st
import pandas as pd
import datetime
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv() 

from data import USERS, RAW_KNOWLEDGE_BASE
from vectorstore import init_vectorstore, get_relevant_documents
from llm_engine import get_generic_response, get_rag_response

if 'audit_log' not in st.session_state:
    st.session_state.audit_log = []

st.set_page_config(page_title="Supra Hospital AI", page_icon="🏥", layout="wide")

# CSS Fix for Theme Compatibility
st.markdown("""
<style>
    .main-header { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; padding: 1.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem; }
    .main-header h1 { color: #38bdf8; font-size: 2rem; margin: 0; }
    
    /* Forces text color to always be dark regardless of system theme */
    .generic-box { background-color: #f1f5f9; border-left: 4px solid #64748b; padding: 1rem; border-radius: 6px; min-height: 200px; color: #0f172a !important; }
    .supra-box { background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 1rem; border-radius: 6px; min-height: 200px; color: #0f172a !important; }
    .alert-denied { background-color: #fef2f2; border-left: 4px solid #dc2626; color: #991b1b; padding: 1rem; border-radius: 6px; }
    
    /* Target nested text elements inside the boxes */
    .generic-box p, .generic-box ul, .generic-box li, .generic-box strong { color: #0f172a !important; }
    .supra-box p, .supra-box ul, .supra-box li, .supra-box strong { color: #0f172a !important; }
</style>
""", unsafe_allow_html=True)

# Initialize and WARM UP Vector DB
@st.cache_resource(show_spinner="Loading AI Knowledge Base into memory (First time only)...")
def load_db():
    vs = init_vectorstore()
    # Forces the embedding model to load immediately so user queries are instant
    vs.similarity_search("warm up", k=1)
    return vs
    
vectorstore = load_db()

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/hospital-2.png", width=64)
st.sidebar.title("Staff Access Portal")
selected_user = st.sidebar.selectbox("Active User Profile:", list(USERS.keys()))
user = USERS[selected_user]
st.sidebar.markdown(f"**Role:** `{user['role']}`")
st.sidebar.markdown(f"**Department:** `{user['dept']}`")
st.sidebar.markdown(f"**Clearance:** `{user['level']}`")

st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Mandatory Demo Queries")

test_queries = [
    "What pain medication should I give a post-TKR patient?",
    "Patient Rajan has knee pain, what should I prescribe?",
    "When should I start DVT prophylaxis after surgery?",
    "What’s our sepsis protocol?",
    "Tell me about Mrs. Padma’s medication management",
    "What is the Ortho Budget for FY2026?",
    "What are the details of our hospital expansion plan?"
]

selected_test = st.sidebar.radio("Select Query to Demo:", test_queries, index=None)

# Main UI
st.markdown("<div class='main-header'><h1>Supra Multi-Specialty Hospital</h1><p>Context-Aware Clinical Decision Support System (RAG Architecture)</p></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💬 Clinical Inquiry Engine", "📚 Knowledge Base & Filters", "🛡️ Audit & Access Logs"])

with tab1:
    user_query = st.text_input("Enter or select a clinical question:", value=selected_test if selected_test else "")

    if st.button("🚀 Run Clinical Evaluation", type="primary"):
        if not user_query:
            st.warning("Please enter a question or select a demo query from the sidebar.")
        else:
            with st.spinner("Executing Vector Search & Groq LLM Inference..."):
                try:
                    retrieved_docs = get_relevant_documents(vectorstore, user_query)
                    
                    generic_res = get_generic_response(user_query)
                    supra_res = get_rag_response(user_query, retrieved_docs, user)
                    
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status = "DENIED" if "ACCESS DENIED" in supra_res else "GRANTED"
                    st.session_state.audit_log.append({
                        "Timestamp": timestamp, 
                        "User": selected_user, 
                        "Role": user['role'],
                        "Query": user_query, 
                        "Access Status": status
                    })
                    
                except Exception as e:
                    st.error(f"Execution Error: {e}")
                    st.stop()

            colA, colB = st.columns(2)
            with colA:
                st.markdown("### 🌐 Standard ChatGPT (Generic)")
                st.markdown(f"<div class='generic-box'>{generic_res}</div>", unsafe_allow_html=True)
                st.caption("⚠️ Generic advice lacks hospital-specific rules and patient contraindications.")
                
            with colB:
                st.markdown("### 🏥 Supra AI (RAG Grounded)")
                st.markdown(f"<div class='supra-box'>{supra_res}</div>", unsafe_allow_html=True)
                st.caption("✅ Grounded in Supra Hospital knowledge, patient safety alerts, and RBAC rules.")
                
                if "ACCESS DENIED" not in supra_res:
                    st.markdown("---")
                    st.markdown("**📄 Grounded Evidence Sources:**")
                    for d in retrieved_docs:
                        st.caption(f"- **{d.metadata['title']}** (Clearance Level: `{d.metadata['access_level']}`)")

with tab2:
    st.subheader("Organizational Knowledge Base")
    st.caption("Browse and filter all 15 active departmental protocols.")
    
    df_kb = pd.DataFrame(RAW_KNOWLEDGE_BASE)
    departments = ["ALL"] + sorted(list(set(df_kb["department"].tolist())))
    selected_dept = st.selectbox("Filter Knowledge Base by Department:", departments)
    
    filtered_df = df_kb[df_kb["department"] == selected_dept] if selected_dept != "ALL" else df_kb
    st.dataframe(filtered_df, use_container_width=True, height=450)

with tab3:
    st.subheader("Security & Access Audit Logs")
    st.caption("Real-time logging of user inquiries and security clearance checks.")
    if st.session_state.audit_log:
        st.dataframe(pd.DataFrame(st.session_state.audit_log), use_container_width=True)
    else:
        st.info("No queries have been executed in this session yet.")