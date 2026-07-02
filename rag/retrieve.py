import chromadb

# ---------------------------------------
# Connect to ChromaDB
# ---------------------------------------

client = chromadb.PersistentClient(
    path="rag/chroma_storage"
)

collection = client.get_collection(
    name="agreement_collection"
)

# ---------------------------------------
# Retrieve Function
# ---------------------------------------

def retrieve_clause(query, top_k=3):

    results = collection.query(

        query_texts=[query],

        n_results=top_k

    )

    return results


# ---------------------------------------
# Test Retrieval
# ---------------------------------------

if __name__ == "__main__":

    print("\n========== AGREEMENT RETRIEVAL ==========\n")

    while True:

        query = input("Enter your query (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = retrieve_clause(query)

        print("\n========== TOP MATCHES ==========\n")

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for i in range(len(documents)):

            print(f"\nResult {i+1}")
            print("-" * 40)

            print("Chunk Number :", metadatas[i]["chunk_number"])
            print("Distance     :", distances[i])

            print("\nClause:\n")
            print(documents[i])

            print("-" * 40)