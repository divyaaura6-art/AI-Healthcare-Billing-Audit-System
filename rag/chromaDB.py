import chromadb

from agree_load import load_agreement
from chunking import chunk_text
from embedding import create_embeddings

# ---------------------------------------
# Create Chroma Client
# ---------------------------------------

client = chromadb.PersistentClient(path="rag/chroma_storage")

# ---------------------------------------
# Delete old collection (for development)
# ---------------------------------------

try:
    client.delete_collection("agreement_collection")
    print("Old collection deleted.")
except:
    print("No previous collection found.")

# ---------------------------------------
# Create new collection
# ---------------------------------------

collection = client.create_collection(
    name="agreement_collection"
)

# ---------------------------------------
# Load Agreement
# ---------------------------------------

agreement_text = load_agreement("docs/agreement.pdf")

# ---------------------------------------
# Create Chunks
# ---------------------------------------

chunks = chunk_text(agreement_text)

# ---------------------------------------
# Generate Embeddings
# ---------------------------------------

embeddings = create_embeddings(chunks)

# ---------------------------------------
# Store Chunks + Embeddings
# ---------------------------------------

for i, chunk in enumerate(chunks):

    collection.add(

        ids=[f"chunk_{i}"],

        documents=[chunk],

        embeddings=[embeddings[i].tolist()],

        metadatas=[
            {
                "chunk_number": i + 1
            }
        ]

    )

# ---------------------------------------
# Verify Database
# ---------------------------------------

print("\n===================================")
print("Agreement Stored Successfully")
print(f"Total Chunks Stored : {collection.count()}")
print("===================================")