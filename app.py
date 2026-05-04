from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)  # ✅ IMPORTANT FIX

# ✅ load embeddings
df = joblib.load("embeddings.joblib")

# ✅ embedding function
def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )
    data = r.json()
    return data["embeddings"]

# ✅ LLM response
def inference(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    return r.json()

# ✅ MAIN API
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")
    top_k = data.get("top_k", 3)

    query_embedding = create_embedding([query])[0]

    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [query_embedding]
    ).flatten()

    indices = similarities.argsort()[::-1][:top_k]
    results = df.loc[indices]

    prompt = f"""
You are an expert Python teacher.

Answer using ONLY the context below.
If context is noisy, give a clear and correct explanation.

Context:
{results[['title','text']].to_string(index=False)}

Question:
{query}

Answer:
"""

    response = inference(prompt)["response"]

    return jsonify({
        "answer": response,
        "sources": list(results["title"])
    })

# ✅ INFO API (for UI)
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "total_chunks": len(df),
        "model": "llama3.2",
        "status": "running"
    })

# ✅ run server
if __name__ == "__main__":
    app.run(debug=True)