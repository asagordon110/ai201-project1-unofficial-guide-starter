import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("utsa_guide")


def retrieve(query, k=4):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results


if __name__ == "__main__":
    query = input("Question: ")

    results = retrieve(query)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][i]["source"]

        print(f"\nSource: {source}")
        print(doc)
        print("-" * 80)