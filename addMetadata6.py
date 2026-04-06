import chromadb

client=chromadb.PersistentClient(path="./chroma_db")

#Creating collectoin with Metadata
collection = client.get_or_create_collection(name="vehicles") 

print("\nCollection Created: ",collection.name)

print()
#Metadata is list of Dictionaries
#Add Metadata along with data to Collection

'''
NOTE

collection.add() DOES NOT UPDATE existing IDs
It IGNORES duplicate IDs silently
Only new IDs get inserted


Wrong->
collection.add(
documents=[
    "Bus is public transport on road",
    "Plane flies in the sky",
    "Boat travels on water",
    "Bicycle travels without fuel"
],
ids=["plane1","bus1","boat1","bike1"],
metadatas=[
    {"type":"air_transport","fuel":"jet"},
    {"type":"public_transport","fuel":"diesel"},
    {"type":"water_transport","fuel":"diesel"},
    {"type":"personal_transport","fuel":"manual"}
]        
)
'''

collection.update(
documents=[
    "Bus is public transport on road",
    "Plane flies in the sky",
    "Boat travels on water",
    "Bicycle travels without fuel"
],
ids=["plane1","bus1","boat1","bike1"],
metadatas=[
    {"type":"air_transport","fuel":"jet"},
    {"type":"public_transport","fuel":"diesel"},
    {"type":"water_transport","fuel":"diesel"},
    {"type":"personal_transport","fuel":"manual"}
]        
)

print("MetaData added Successfully.\n")

data = collection.get(include=["documents","metadatas"])  #ids added bydefault

print("\nCurrent Data & Metadata: ")
print()
for i, doc, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"{i} -> {doc} | {meta}")