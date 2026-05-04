import os
import json

INPUT_FOLDER = "jsons"
OUTPUT_FOLDER = "final_chunks"

# create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def merge_chunks(chunks, max_words=120):
    merged = []
    current_text = ""
    current_meta = None

    for chunk in chunks:
        text = chunk["text"].strip()

        if not current_meta:
            current_meta = {
                "number": chunk["number"],
                "title": chunk["title"],
                "start": chunk["start"]
            }

        current_text += " " + text

        if len(current_text.split()) >= max_words:
            merged.append({
                "number": current_meta["number"],
                "title": current_meta["title"],
                "start": current_meta["start"],
                "end": chunk["end"],
                "text": current_text.strip()
            })
            current_text = ""
            current_meta = None

    # leftover chunk
    if current_text and current_meta:
        merged.append({
            "number": current_meta["number"],
            "title": current_meta["title"],
            "start": current_meta["start"],
            "end": chunk["end"],
            "text": current_text.strip()
        })

    return merged


files = os.listdir(INPUT_FOLDER)

for file in files:
    if file.endswith(".json"):
        path = os.path.join(INPUT_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            chunks = data["chunks"]

        merged_chunks = merge_chunks(chunks)

        output_path = os.path.join(OUTPUT_FOLDER, file)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"chunks": merged_chunks}, f, indent=4, ensure_ascii=False)

        print(f"Processed: {file}")

print("✅ Chunk optimization done")