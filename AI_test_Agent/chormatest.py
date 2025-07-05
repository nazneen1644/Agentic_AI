import chromadb
client = chromadb.Client()
collection = client.create_collection(name="test")
collection.add(documents=["hello world"], ids=["id1"])
print(collection.query(query_texts=["hello"], n_results=1))