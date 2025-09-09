# RAG-based LLM Chatbot for Natural Language Querying over BigQuery

This project is a Retrieval-Augmented Generation (RAG) chatbot designed to help marketing teams query customer segmentation data (RFM) stored in Google BigQuery using natural language, without needing SQL knowledge.
By combining Large Language Models (LLM) with semantic retrieval over tabular data, this chatbot improves operational efficiency and makes data querying more intuitive and accessible.

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot designed to help marketing teams query customer segmentation data (RFM) stored in Google BigQuery using natural language, without needing SQL knowledge.
By combining Large Language Models (LLM) with semantic retrieval over tabular data, this chatbot improves operational efficiency and makes data querying more intuitive and accessible.

## Key Features

🔹 Natural Language Querying – Ask questions in plain English without writing SQL.

🔹 BigQuery Integration – Data is fetched directly from Google BigQuery.

🔹 RFM Segmentation Support – Built specifically for customer segmentation analysis.

🔹 RAG Pipeline – Embeds structured tabular data with SentenceTransformer and retrieves via FAISS.

🔹 Streamlit UI – Simple web-based interface for real-time interaction.

🔹 LLaMA via GroqCloud API – Fast, scalable inference with LLaMA-3 70B model.

## Tech Stack
🔹 Language Model API: GroqCloud (LLaMA-3-70B-8192)

🔹 Vector Database: FAISS
🔹 Embedding Model: SentenceTransformers (HuggingFace)

🔹 Data Warehouse: Google BigQuery

🔹 Frameworks & Tools: LangChain, Streamlit, Python

## Architecture
1. Data Loading → Load RFM segmentation data from BigQuery with google.cloud.bigquery.
2. Embedding & Indexing → Convert structured data into embeddings using SentenceTransformer, indexed with FAISS.
3. Retrieval & Augmentation → Retrieve relevant chunks for context-aware answering.
4. LLM Inference → Query handled by GroqCloud LLaMA for natural language response.
5. User Interface → Streamlit app for real-time chatbot interaction.

## Instalation

1. After cloning this repository, please create a folder named "ytta" or any name you like in order to store secret.toml file (this is where API KEY located)
2. Create credentials.json in order to get access to database and table from BigQuery. link: https://docs.google.com/document/d/10Q3JamUmVbxALnET7m_f_VZp0J1BukoHVmLIk0AWWuo/edit?usp=sharing
3. Create virtual environment
4. Install all requirements with pip install -r requirements.txt
5. Run the streamlit application


