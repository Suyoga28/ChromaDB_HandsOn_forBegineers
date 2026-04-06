import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collections=client.list_collections()
print("\nAll available collection\n")

for c in collections:
    print("-", c.name)
