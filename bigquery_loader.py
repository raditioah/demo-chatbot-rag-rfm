from google.cloud import bigquery
import pandas as pd
import os

def load_bigquery_data():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/projek_mandiri/hack_bootcamp/rag_chatbot/credentials.json"
    client = bigquery.Client()
    query = """
    SELECT *
    FROM `data-pipeline-rfm.db_rfm.tbl_rfm_fix`
    """
    df = client.query(query).to_dataframe()
    df.dropna(inplace=True)
    return df