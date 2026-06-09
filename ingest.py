from pathlib import Path
import re
import json

DOCUMENTS_DIR = Path("documents")
OUTPUT_FILE = Path("chunks.json")

CHUNK_SIZE = 800
OVERLAP = 100


def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&amp;", "&")
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if len(chunk) > 50:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def load_documents():
    all_chunks = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        raw_text = file_path.read_text(encoding="utf-8")
        cleaned = clean_text(raw_text)
        chunks = chunk_text(cleaned)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "id": f"{file_path.stem}_{i}",
                "source": file_path.name,
                "chunk_index": i,
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":
    chunks = load_documents()

    OUTPUT_FILE.write_text(
        json.dumps(chunks, indent=2),
        encoding="utf-8"
    )

    print(f"Created {len(chunks)} chunks.")
    print("\nSample chunks:\n")

    for chunk in chunks[:5]:
        print(f"Source: {chunk['source']}")
        print(chunk["text"])
        print("-" * 80)