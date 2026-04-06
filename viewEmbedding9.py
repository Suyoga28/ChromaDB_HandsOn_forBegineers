#Chroma automatically generate embedding.
#what if as developer i want to check whether embeddings are automatically or not?

import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_collection("vehicles")

data = collection.get(include=["documents","embeddings"])

print("\nCurrent data with Embeddings: ")
print()
for i, doc, embed in zip(data["ids"], data["documents"], data["embeddings"]):
    print(f"\n{i} -> {doc}")
    print(f"Embedding (first 10 values): {embed[:10]}")



