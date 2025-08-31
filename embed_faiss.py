from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

import pandas as pd

def create_faiss_index(df):
    # Buat teks representatif dari tiap baris
    df['text'] = df.apply(lambda row: 
        f"Pelanggan {row['Customer ID']} dari {row['Country']} merupakan pelanggan {row['Segment']} dengan nilai Recency={row['Recency']}, Frequency={row['Frequency']}, Monetary={row['Monetary']}", 
        axis=1
    )

    # Konversi ke LangChain Document
    docs = [Document(page_content=row['text'], metadata={"Customer ID": row['Customer ID']}) for _, row in df.iterrows()]
    
    # Buat embedding
    embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Buat dan kembalikan vectorstore FAISS
    faiss_index = FAISS.from_documents(docs, embedding_model)
    return faiss_index



