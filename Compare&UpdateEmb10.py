import numpy as np
import chromadb

#Cosine output
# 1 = very similar
# 0 = unrelated
# -1 = opposite 


def cosine_similarity(vec1,vec2):
    return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))

client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_collection("vehicles")

data = collection.get(include=["documents","embeddings"])

#Get embeddings
emb_car=data["embeddings"][0]
emb_plane=data["embeddings"][1]
emb_bus=data["embeddings"][2]

sim_car_plane = cosine_similarity(emb_car,emb_plane)
sim_car_bus = cosine_similarity(emb_car,emb_bus)

print("\nCosine Smilarities ")
print(f"Car VS Plane : {sim_car_plane:.4f}")
print(f"Car VS Bus : {sim_car_bus:.4f}")

'''
Output before updating document-
Cosine Smilarities
Car VS Plane : 0.1894
Car VS Bus : 0.2018
'''
#Updating Document now embeddings should also be updated automatically
#old doc for car:Car runs on land 

collection.update(
    ids=["car1","plane1","bus1"],
    documents=["Car runs on road using electricity as fuel.","Plane flies high in sky.","Bus is public transport that runs on road."]
)
print("\nDocument updated successfully.")

'''
run program 2nd time to see changes in cosine similarity 
New output:

Cosine Smilarities
Car VS Plane : -0.0112
Car VS Bus : 0.4044

Document updated successfully.
'''



