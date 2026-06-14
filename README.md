# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

### Question 1

**Question:** What advice do students give for internships?

**Expected Answer:** Students should prepare early, maintain a strong resume, GitHub, LinkedIn profile, portfolio, practice technical interview skills, and develop behavioral interview stories.

**System Response:** Students recommend preparing for internships before applications open by having a strong resume, LinkedIn profile, GitHub, and portfolio. They also suggest practicing technical interview skills and preparing behavioral interview stories.

**Retrieved Sources:**

* utsa_internship_advice_1.txt
* utsa_campus_resources_2.txt

**Accuracy:** Accurate

---

### Question 2

**Question:** How should students study for CS exams?

**Expected Answer:** Students should review lecture slides, homework, labs, coding exercises, and practice problems regularly rather than cramming.

**System Response:** The system recommended reviewing lecture materials, practicing coding exercises, and studying consistently in short sessions.

**Retrieved Sources:**

* utsa_study_advice_1.txt
* utsa_cs_courses_1.txt

**Accuracy:** Accurate

---

### Question 3

**Question:** What makes a professor helpful?

**Expected Answer:** Clear explanations, responsiveness, detailed feedback, office hours, examples, and structured expectations.

**System Response:** The system identified helpful professors as those who provide examples, clear expectations, useful feedback, and are responsive to student questions.

**Retrieved Sources:**

* utsa_cs_professors_1.txt
* utsa_cs_professors_2.txt

**Accuracy:** Accurate

---

### Question 4

**Question:** What advice is given to new CS students?

**Expected Answer:** Make friends early, ask questions, avoid comparing yourself to others, and seek help when needed.

**System Response:** The system summarized recommendations about making connections with classmates, asking questions, and focusing on personal improvement.

**Retrieved Sources:**

* utsa_new_student_advice_1.txt

**Accuracy:** Accurate

---

### Question 5

**Question:** What campus resources do students recommend?

**Expected Answer:** Tutoring, academic support, library study spaces, career fairs, mock interviews, and resume reviews.

**System Response:** The system highlighted tutoring, academic support, library resources, career fairs, and interview preparation services.

**Retrieved Sources:**

* utsa_campus_resources_1.txt
* utsa_campus_resources_2.txt

**Accuracy:** Accurate

Question 2

Question: How should students study for CS exams?

Expected Answer: Students should review lecture slides, homework, labs, coding exercises, and practice problems regularly rather than cramming.

System Response: The system recommended reviewing lecture materials, practicing coding exercises, and studying consistently in short sessions.

Retrieved Sources:

utsa_study_advice_1.txt
utsa_cs_courses_1.txt

Accuracy: Accurate

Question 3

Question: What makes a professor helpful?

Expected Answer: Clear explanations, responsiveness, detailed feedback, office hours, examples, and structured expectations.

System Response: The system identified helpful professors as those who provide examples, clear expectations, useful feedback, and are responsive to student questions.

Retrieved Sources:

utsa_cs_professors_1.txt
utsa_cs_professors_2.txt

Accuracy: Accurate

Question 4

Question: What advice is given to new CS students?

Expected Answer: Make friends early, ask questions, avoid comparing yourself to others, and seek help when needed.

System Response: The system summarized recommendations about making connections with classmates, asking questions, and focusing on personal improvement.

Retrieved Sources:

utsa_new_student_advice_1.txt

Accuracy: Accurate

Question 5

Question: What campus resources do students recommend?

Expected Answer: Tutoring, academic support, library study spaces, career fairs, mock interviews, and resume reviews.

System Response: The system highlighted tutoring, academic support, library resources, career fairs, and interview preparation services.

Retrieved Sources:

utsa_campus_resources_1.txt
utsa_campus_resources_2.txt

Accuracy: Accurate

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

## Failure Case Analysis

### Question

Who is the president of UTSA?

### Expected Behavior

The system should refuse to answer because this information is not present in the document collection.

### System Response

"I don't have enough information to answer that."

### Analysis

Failure Case Analysis
Question

Who is the president of UTSA?

Expected Behavior

The system should refuse to answer because this information is not present in the document collection.

System Response

"I don't have enough information to answer that."

Analysis

This behavior is considered successful grounding, but it also reveals a limitation of the retrieval corpus. Because the project only contains student-generated advice and not university administrative information, the retrieval stage returned loosely related chunks from career and study documents. The LLM correctly followed the grounding instructions and refused to answer. In a larger production system, this limitation could be addressed by expanding the document collection or adding metadata filtering to separate different knowledge domains.



**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

The planning document was helpful because it forced me to think about my document sources, chunking strategy, retrieval approach, and evaluation plan before writing code. Having these decisions documented made implementation much easier because I already knew what tools and architecture I wanted to use.

One area where implementation differed from the original plan was the chunking strategy. Initially, I used fixed character chunking, but this produced chunks that split words and reduced readability. During development, I switched to sentence-based chunking with overlap, which produced more meaningful chunks and improved retrieval quality.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

ChatGPT and Claude were used to help implement the ingestion and chunking pipeline. The generated code was reviewed and modified to improve chunk quality and prevent words from being split across chunks.



**Instance 2**

ChatGPT was used to assist with ChromaDB integration and Groq API implementation. Generated examples were adapted to fit the project's architecture and grounding requirements.
