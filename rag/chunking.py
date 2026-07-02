from agree_load import load_agreement


def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":

    agreement_text = load_agreement("docs/agreement.pdf")

    chunks = chunk_text(agreement_text)

    print("\n========== CHUNKS ==========\n")

    for i, chunk in enumerate(chunks):

        print(f"\n----- Chunk {i+1} -----\n")

        print(chunk)