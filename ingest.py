from pathlib import Path
import re
import json

DOCUMENTS_DIR = Path("documents")
OUTPUT_FILE = Path("chunks.json")

CHUNK_SIZE = 800
OVERLAP = 1


def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&amp;", "&")
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=800, overlap_sentences=1):
    chunks = []

    sentences = re.split(r'(?<=[.!?])\s+', text)
    current_sentences = []
    current_length = 0

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        sentence_length = len(sentence)

        if current_length + sentence_length <= chunk_size:
            current_sentences.append(sentence)
            current_length += sentence_length
        else:
            chunk = " ".join(current_sentences).strip()

            if len(chunk) > 50:
                chunks.append(chunk)

            current_sentences = current_sentences[-overlap_sentences:] if current_sentences else []
            current_sentences.append(sentence)
            current_length = sum(len(s) for s in current_sentences)

    final_chunk = " ".join(current_sentences).strip()

    if len(final_chunk) > 50:
        chunks.append(final_chunk)

    return chunks


def load_documents():
    all_chunks = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        raw_text = file_path.read_text(encoding="utf-8")
        cleaned = clean_text(raw_text)
        chunks = chunk_text(cleaned, CHUNK_SIZE, OVERLAP)

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