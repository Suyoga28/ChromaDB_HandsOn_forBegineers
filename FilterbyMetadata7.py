import chromadb

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_collection("vehicles")

#Example 1: Filter by transport type
public_transport = collection.get(where={"type":"public_transport"})
print("\npublic Transport: ")
print(public_transport)

#Example 2: Filter by fuel type
diesel_vehicles = collection.get(where={"fuel":"diesel"})
print("\nDiesel Vehicles: ")
print(diesel_vehicles)



