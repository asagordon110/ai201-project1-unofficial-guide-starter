# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

My domain is an unofficial UTSA CS student guide. The system will help students search student-generated advice about CS classes, professors, studying, campus resources, and course difficulty. This knowledge is valuable because official UTSA pages describe course requirements, but they do not explain what students actually experience.


---

## Documents

I will collect at least 10 text documents from student-generated or student-centered sources, including professor reviews, Reddit discussions, course advice posts, and personal notes about CS classes.

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

---

## Chunking Strategy

I will chunk documents by paragraph where possible, then group nearby paragraphs until each chunk is around 500–800 characters. I will use about 100 characters of overlap so that advice split between paragraphs is not lost. This fits my documents because student reviews are usually short and opinion-based, so chunks should stay focused on one professor, course, or piece of advice.

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

I will use sentence-transformers with all-MiniLM-L6-v2 for embeddings and ChromaDB as the vector store. I will retrieve the top 4 or 5 chunks for each query. If this were a production system, I would compare embedding models based on accuracy, speed, cost, context length, and ability to handle student slang or informal language.

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question                                             | Expected answer |
|---|----------|-------------------------------------------|
| 1 |  Which CS courses do students describe as difficult? | The system should identify specific courses mentioned in the documents and explain why students found them difficult.
|
| 2 | What do students say about preparing for exams?      | The system should summarize student advice about studying, reviewing lecture notes, practice problems, or attending class. |
| 3 | Which professors are described as helpful?           | The system should name professors only if they appear in the documents and cite the source. |
| 4 | What advice do students give to new CS majors?       | The system should summarize advice from the collected student sources. |
| 5 | What campus resources do students recommend?         | The system should mention only resources found in the documents. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. One challenge is that student-generated content may be noisy, informal, or inconsistent. 

2. Another challenge is that chunks may accidentally split useful context, causing retrieval to return incomplete answers.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->


     ## Architecture

```mermaid
flowchart LR
    A[Document Ingestion<br>Local TXT files] --> B[Chunking<br>Paragraph-based chunks]
    B --> C[Embedding<br>all-MiniLM-L6-v2]
    C --> D[Vector Store<br>ChromaDB]
    D --> E[Retrieval<br>Top-k relevant chunks]
    E --> F[Generation<br>Groq Llama 3.3 70B]

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     I will use ChatGPT to help implement the document ingestion and chunking functions based on my chunking strategy. I will also use ChatGPT and Claude to help debug the ChromaDB retrieval code and improve the grounded response prompt, but I will review and edit the code myself.

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
