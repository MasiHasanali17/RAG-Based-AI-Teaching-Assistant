# 🚀 RAG-Based AI Teaching Assistant

An AI-powered teaching assistant that answers questions from video lecture transcripts using **Retrieval-Augmented Generation (RAG)** and a **local LLM (Ollama)**.

This system allows users to query course content naturally and receive **accurate, context-aware answers along with source references**.

---

## 💡 Sample Questions

You can try asking:

* What is Python?
* What is Python list?
* In which lecture are loops taught?
* Explain functions in Python
* Where is OOP explained?
* What is recursion in Python?

---

## 🧠 Features

* 💬 Chat-based UI (similar to ChatGPT)
* 🔍 Semantic search using vector embeddings
* 📚 Answers grounded in lecture transcripts
* 📌 Displays source lectures for transparency
* ⚡ Fast retrieval using precomputed embeddings
* 🖥️ Fully local setup (no API key required)

---

## 🏗️ Tech Stack

### 🔹 Backend

* Python
* Flask
* Flask-CORS

### 🔹 AI / ML

* Ollama (Local LLM runtime)
* LLaMA 3.2 (text generation)
* BGE-M3 (embeddings model)
* Scikit-learn (cosine similarity)

### 🔹 Data Processing

* Pandas
* NumPy
* Joblib

### 🔹 Frontend

* HTML
* CSS
* JavaScript

---

## ⚙️ How It Works (Step-by-Step)

### 1. 🎥 Video Processing

* Videos → audio (`process_video.py`)
* Audio → transcript chunks

### 2. ✂️ Chunking

* Split transcripts (`create_chunks.py`)
* Optimize chunks (`optimized_chunks.py`)

### 3. 🧠 Embedding Creation

* Convert chunks → embeddings (BGE-M3)
* Save using:

  * `batch_embeddings.py`
  * `save_embeddings.py`

### 4. 🔍 Retrieval (RAG)

* Convert user query → embedding
* Find top relevant chunks using cosine similarity

### 5. 🤖 Generation

* Send retrieved chunks + query → LLaMA 3.2
* Generate final answer

### 6. 🌐 UI Interaction

* User asks question via `index.html`
* Backend (`app.py`) processes and returns response

---

## 📁 Project Structure

```text
RAG-Based-AI-Teaching-Assistant/
│
├── app.py
├── index.html
├── embeddings.joblib
│
├── batch_embeddings.py
├── save_embeddings.py
├── create_chunks.py
├── optimized_chunks.py
├── process_video.py
│
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Ollama

👉 https://ollama.com

```bash
ollama pull llama3.2
ollama pull bge-m3
```

### 3. Run backend

```bash
python app.py
```

### 4. Run frontend

* Open `index.html`
* OR use Live Server

### 5. Ask questions 🎯

---

## ⚠️ Notes

* Ollama must be running locally
* Embeddings must exist before running app
* Fully offline system (no API usage)

---

## 🚀 Future Improvements

* Better transcript cleaning
* Stronger prompt engineering
* Chat history support
* Deployment (Streamlit / cloud)
* Clickable timestamps

---

## 📌 Project Type

**Retrieval-Augmented Generation (RAG) System for Education**

---

## 🙌 Author

Built to explore:

* RAG systems
* Local LLM integration
* Full-stack AI applications

---

⭐ If you like this project, consider giving it a star!
