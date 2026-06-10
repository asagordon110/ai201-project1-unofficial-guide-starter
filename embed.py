import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="utsa_guide"
)

# Add chunks
for chunk in chunks:
    embedding = model.encode(chunk["text"]).tolist()

    collection.add(
        ids=[chunk["id"]],
        embeddings=[embedding],
        documents=[chunk["text"]],
        metadatas=[{
            "source": chunk["source"],
            "chunk_index": chunk["chunk_index"]
        }]
    )

print(f"Added {len(chunks)} chunks to ChromaDB")