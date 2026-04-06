#chromadb.errors.NotFoundError: Collection [vehicles] does not exist
#Persistent Client - store data in disk/folder instead of memory



import chromadb
#client=chromadb.Client()
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_collection("vehicles")
print(collection.get())

#printing using loop

data = collection.get()

print("\nCurrent data: ")
print()
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")