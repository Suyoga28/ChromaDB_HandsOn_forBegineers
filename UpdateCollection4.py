import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection("vehicles")

collection.update(
    ids=["bus1"],
    documents=["Bus carries more than 40 passengers and runs on roads"]
)

record = collection.get(ids=["bus1"])
print(record)