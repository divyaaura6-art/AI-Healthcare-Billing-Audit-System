import chromadb

client = chromadb.PersistentClient(path="rag/chroma_storage")

collection = client.get_collection("agreement_collection")

print("Number of Chunks :", collection.count())

data = collection.peek()

print("\nFirst Chunk:\n")
print(data["documents"][0])

print("\nMetadata:\n")
print(data["metadatas"][0])