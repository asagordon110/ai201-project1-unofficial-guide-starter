import os
import chromadb

from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    "utsa_guide"
)


def retrieve(query, k=4):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    return results


def ask(question):
    retrieved = retrieve(question)

    docs = retrieved["documents"][0]
    metadata = retrieved["metadatas"][0]

    context = "\n\n".join(docs)

    prompt = f"""
You are an assistant for the UTSA Student Guide.

Answer ONLY using the provided context.

If the answer is not contained in the context,
respond with:

"I don't have enough information to answer that."

Context:

{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    sources = list(
        set(meta["source"] for meta in metadata)
    )

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    question = input("Question: ")

    result = ask(question)

    print("\nANSWER:\n")
    print(result["answer"])

    print("\nSOURCES:")
    for source in result["sources"]:
        print("-", source)