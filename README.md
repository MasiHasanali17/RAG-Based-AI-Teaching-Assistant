# 🚀 RAG-Based AI Teaching Assistant

An AI-powered teaching assistant that answers questions from video lecture transcripts using **Retrieval-Augmented Generation (RAG)** and a **local LLM (Ollama)**.

This project allows users to ask questions like:

* *“What is Python?”*
* *“Where are loops taught?”*

…and get answers along with **relevant lecture sources**.

---

## 🧠 Features

* 💬 Chat-based UI (like ChatGPT)
* 🔍 Semantic search using embeddings
* 📚 Answers grounded in lecture transcripts
* 📌 Shows source lectures for answers
* ⚡ Fast retrieval using precomputed embeddings
* 🖥️ Fully runs locally (no API key required)

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
* Joblib (saving embeddings)

### 🔹 Frontend

* HTML
* CSS
* JavaScript

---

## ⚙️ How It Works (Step-by-Step)

### 1. 🎥 Video Processing

* Videos are converted into audio (`process_video.py`)
* Audio is transcribed into text chunks

### 2. ✂️ Chunking

* Transcripts are split into smaller chunks (`create_chunks.py`)
* Optimized chunks are generated (`optimized_chunks.py`)

### 3. 🧠 Embedding Creation

* Each chunk is converted into vector embeddings using **BGE-M3**
* Stored using:

  * `batch_embeddings.py`
  * `save_embeddings.py`
* Final data saved as:

  ```text
  embeddings.joblib
  ```

### 4. 🔍 Retrieval (RAG)

* User question → converted into embedding
* Cosine similarity is used to find top relevant chunks

### 5. 🤖 Generation

* Retrieved chunks + user query → sent to LLM (LLaMA 3.2)
* LLM generates final answer using context

### 6. 🌐 UI Interaction

* User interacts via web UI (`index.html`)
* Backend (`app.py`) processes request and returns answer

---

## 📁 Project Structure

```text
RAG-Based-AI-Teaching-Assistant/
│
├── app.py                 # Flask backend (main API)
├── index.html             # Frontend UI
├── embeddings.joblib      # Precomputed embeddings
│
├── batch_embeddings.py    # Generate embeddings
├── save_embeddings.py     # Save embeddings
├── create_chunks.py       # Create chunks from transcripts
├── optimized_chunks.py    # Improve chunk quality
├── process_video.py       # Convert video to audio
│
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## ▶️ How to Run the Project

### 1. 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. 🤖 Install and Run Ollama

Download Ollama from:
👉 https://ollama.com

Run:

```bash
ollama pull llama3.2
ollama pull bge-m3
```

---

### 3. ▶️ Start Backend Server

```bash
python app.py
```

You should see:

```text
Running on http://127.0.0.1:5000
```

---

### 4. 🌐 Run Frontend

* Open `index.html` in browser
  OR
* Use Live Server (VS Code)

---

### 5. 💬 Ask Questions

Example:

* What is Python?
* Where are loops taught?

---

## ⚠️ Notes

* Ensure Ollama is running locally
* Embeddings must be generated before running app
* No API key required (fully local setup)

---

## 🚀 Future Improvements

* Better transcript cleaning
* Improved prompt engineering
* Chat history memory
* Deployment (cloud)
* Clickable timestamps for lectures

---

## 📌 Project Type

This is a **Retrieval-Augmented Generation (RAG)** based AI system designed for educational use.

---

## 🙌 Author

Built as part of an AI learning project to understand:

* RAG systems
* LLM integration
* Full-stack AI application development

---

