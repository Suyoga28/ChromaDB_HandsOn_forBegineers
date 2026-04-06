import chromadb
#client = chromadb.Client()

#Persistent Client - store data in disk/folder instead of memory
client=chromadb.PersistentClient(path="./chroma_db")

#Creating collectoin
collection = client.create_collection(name="vehicles") 

print("\nCollection Created: ",collection.name)

print()

#Add data to Collection
collection.add(
documents=[
    "Car runs on land",
    "Plane flies in the sky",
    "Boat travels on water",
    "Bus is public transport on road"
],
ids=["car1","plane1","boat1","bus1"]        
)

print("Data added Permanantly in folder chroma_db.\n")