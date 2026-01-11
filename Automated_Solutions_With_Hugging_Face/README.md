# Automated Solutions with Hugging Face 🤗

This directory contains practical, end-to-end examples of **LLM inference and interaction patterns**
using the Hugging Face Transformers ecosystem, optimized for **Colab environments** and limited GPUs
(e.g. T4).

The focus is on **how model outputs are generated and streamed**, not just on model accuracy.

---

## 📘 Notebook: Response Output Modes

**File:** `Response_output_modes.ipynb`

This notebook demonstrates and compares **three different LLM response generation strategies** using
an instruction-tuned LLaMA model loaded with **4-bit quantization**.

### Covered output modes

1. **Full Response Generation**
   - The model generates the entire response before returning it.
   - Simple to implement but introduces latency for long outputs.

2. **Low-Level Streaming (Token-by-Token)**
   - Tokens are generated manually using model logits.
   - Offers maximum control but is harder to maintain and optimize.

3. **High-Level Streaming (TextIteratorStreamer)**
   - Uses Hugging Face’s built-in streaming utilities.
   - Clean, efficient, and suitable for real-world applications.

---

## 🧠 What this notebook demonstrates

- Loading large instruction-tuned models with **4-bit quantization (BitsAndBytes)**
- Differences between **blocking vs streaming inference**
- Trade-offs between **low-level control and high-level abstractions**
- Streaming-friendly architecture for **interactive applications**
- Integration of **Gradio** with token streaming

---

## 🚀 How to run

This notebook is designed to run on **Google Colab**.

**Recommended runtime:**
- GPU: **T4**
- Python: default Colab environment

### Open in Colab
> GitHub preview may fail due to streaming widgets.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/maram-atia/llm-eng-Solutions/blob/main/Automated_Solutions_With_Hugging_Face/Response_output_modes.ipynb
)

---

## ⚠️ GitHub preview note

This notebook uses **streaming, threading, and interactive widgets**.
As a result, GitHub may display an *“Invalid Notebook”* preview error.

➡️ This does **not** affect execution.  
➡️ Please open the notebook in **Google Colab** to run it properly.

---

## 🔧 Requirements (installed in notebook)

- `transformers`
- `torch`
- `bitsandbytes`
- `accelerate`
- `sentencepiece`
- `gradio`

All dependencies are installed directly inside the notebook.

---

## 🎯 Learning goal

This notebook is part of a broader effort to build **LLM engineering intuition** around:
- inference efficiency
- user experience (latency vs responsiveness)
- production-oriented generation patterns
