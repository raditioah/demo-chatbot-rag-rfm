# app.py
import streamlit as st
import toml
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

from bigquery_loader import load_bigquery_data
from embed_faiss import create_faiss_index

# ===================== Load API Key =====================
secrets = toml.load("ytta/secret.toml")
api_key = secrets.get("LLM_API_KEY")

# ===================== Load Data =====================
st.title("Chatbot RAG dengan FAISS + BigQuery")
df = load_bigquery_data()
st.success("Data berhasil dimuat dari BigQuery!")

# ===================== FAISS Index =====================
st.write("Membangun FAISS index...")
vector_db = create_faiss_index(df)
st.success("Index FAISS siap digunakan.")

# ===================== Inisialisasi LLM =====================
llm = ChatGroq(api_key=api_key, model="llama3-70b-8192", temperature=0.7)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Anda adalah asisten AI yang menjawab berdasarkan data pelanggan berikut:

    {context}

    Jawaban atas pertanyaan ini:
    {question}
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

# ===================== State =====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ===================== Chat UI =====================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===================== Input & Retrieval =====================
if query := st.chat_input("Silakan tanya tentang pelanggan..."):
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("Mencari jawaban..."):
        docs = vector_db.similarity_search(query, k=5)
        context = "\n".join([doc.page_content for doc in docs])
        response = chain.run(context=context, question=query)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
