import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection("vehicles")

collection.delete(
    ids=["boat1"],
)

data=collection.get()

print("\nRemaing data: ")
print()
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")