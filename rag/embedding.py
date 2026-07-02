from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":

    from agree_load import load_agreement
    from chunking import chunk_text

    agreement = load_agreement("docs/agreement.pdf")

    chunks = chunk_text(agreement)

    embeddings = create_embeddings(chunks)

    print("Total Chunks :", len(chunks))
    print("Embedding Shape :", embeddings.shape)