import chromadb
client = chromadb.Client()

#Create collectoin
collection = client.create_collection(name="vehicles") 

print("Collection Created: ",collection.name)

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

print()

#Query the Collection
results = collection.query(
query_texts=["vehicle that run on road"],  
n_results=2  
)

#print the output
print(results,"\n")


