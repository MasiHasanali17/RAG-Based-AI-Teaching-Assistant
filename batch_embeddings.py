import requests
import os
import json
import pandas as pd

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )
    
    data = r.json()
    
    if "embeddings" not in data:
        print("ERROR:", data)
        exit()
    
    return data["embeddings"]

folder = "final_chunks"
all_chunks = []
chunk_id = 0

files = os.listdir(folder)

for file in files:
    if file.endswith(".json"):
        with open(os.path.join(folder, file), encoding="utf-8") as f:
            content = json.load(f)

        print(f"Creating embeddings for {file}")

        texts = [c["text"] for c in content["chunks"]]

        embeddings = create_embedding(texts)

        for i, chunk in enumerate(content["chunks"]):
            chunk["chunk_id"] = chunk_id
            chunk["embedding"] = embeddings[i]
            chunk_id += 1
            all_chunks.append(chunk)

df = pd.DataFrame.from_records(all_chunks)

df.to_json("final_embeddings.json", orient="records", indent=4)

print("✅ Done")
print("Total chunks:", len(df))