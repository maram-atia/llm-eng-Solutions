# 📁 RAG_Solutions

This directory contains my practical work on Retrieval-Augmented Generation (RAG) systems, covering the full journey from fundamentals and experimentation (notebooks) to production-style Python implementations and evaluation.

The project follows a progressive learning path, moving from basic RAG concepts to modular, reusable, and evaluatable RAG pipelines.

## 📂 Project Structure

```
RAG_Solutions/
│
├── evaluation/
│   ├── eval.py            # RAG evaluation logic
│   ├── test.py            # Test cases for RAG outputs
│   └── tests.jsonl        # Golden test dataset
│
├── knowledge-base/        # Source documents used for RAG
│
├── langchain_Solution/
│   ├── part1.ipynb        # RAG fundamentals & simple pipelines
│   └── part2.ipynb        # Complete RAG pipeline with LangChain
│
├── preprocessed_db/       # Chunked & processed documents
│
├── pro_implementation/
│   ├── ingest.py          # Data ingestion & vectorization
│   └── answer.py          # RAG query answering pipeline
│
├── vector_db/             # Vector database (Chroma / FAISS)
│
├── evaluator.py           # End-to-end RAG evaluation runner
└── Rag_Solution.ipynb     # High-level RAG experimentation notebook
```

## 🧠 langchain_Solution/

This directory contains notebook-based implementations using LangChain to explore and understand RAG concepts.

**Covers:**
- Document loading and chunking
- Vector embeddings
- Vector stores
- Retriever + LLM integration
- End-to-end RAG pipelines

📌 *These notebooks focus on learning, experimentation, and debugging.*

## ⚙️ pro_implementation/

This directory contains a production-oriented RAG implementation written as Python scripts, not notebooks.

**Key characteristics:**
- Modular code structure
- Clear separation between ingestion and inference
- Designed to be reusable and extensible
- Closer to how RAG systems are built in real applications

📌 *This represents the transition from experimentation to production-ready RAG.*

## 📊 evaluation/

This directory is dedicated to evaluating RAG performance.

**Includes:**
- Golden datasets (`tests.jsonl`)
- Automated evaluation scripts
- Comparison of RAG outputs against expected answers

📌 *Evaluation is treated as a core component of the system.*

## 🎯 Goals of This Project

- Understand RAG fundamentals and best practices
- Build complete RAG pipelines using LangChain
- Design modular, production-style RAG systems
- Evaluate retrieval and generation quality systematically

## 🧩 Technologies Used

- Python
- LangChain
- Vector Databases (Chroma / FAISS)
- OpenAI / Encoder Embedding Models
- JSONL evaluation datasets

---

**Note:** This project demonstrates the complete lifecycle of building RAG systems—from initial experimentation to production deployment and evaluation.
