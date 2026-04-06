import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_collection("vehicles")


res = collection.query(
    query_texts=["vehicle that doesn't need fuel"],
    n_results=2
)

# Lower the distance = Higher the similarity and Ranking
print("Semantic Search Results: ")
for doc, dist in zip(res["documents"][0],res["distances"][0]):
    print(f" {doc} (distance: {dist: .4f})")
    
    
    