from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv(r"C:\Users\NAZNEEN\Downloads\realistic_restaurant_reviews.csv")
embeddings  = OllamEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        text = row['review']
        doc = Document(page_content= row["Title"] +" " + row["Review"], metadata={"rating": row['Rating'], "date": row['Date']}, id = str(i))
        documents.append(documents)
        ids.append(str(i))

vector_store = Chrome(
    collection_name="restaurant_reviews",
    embedding_function=embeddings,
    persist_directory=db_location,
    
)

if add_documents:
    vector_store.add_documents(documents, ids=ids)

retriever = vector_store.as_retriever(
   
    search_kwargs={"k": 10}

)