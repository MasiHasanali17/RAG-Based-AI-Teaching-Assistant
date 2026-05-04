import whisper
import json
import os

model = whisper.load_model("tiny")

audio_folder = "audios"
output_folder = "jsons"

os.makedirs(output_folder, exist_ok=True)

files = os.listdir(audio_folder)

for file in files:
    if file.endswith(".mp3"):

        audio_path = os.path.join(audio_folder, file)

        file_name = os.path.splitext(file)[0]

        number = "Unknown"
        title = file_name

        if "Lecture" in file_name:
            parts = file_name.split("_")
            if len(parts) > 0:
                number = parts[0].replace("Lecture", "").strip()
                title = file_name

        print(f"Processing: {file}")

        result = model.transcribe(
            audio=audio_path,
            task="transcribe",
            word_timestamps=False
        )

        chunks = []

        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

        data = {
            "chunks": chunks,
            "text": result["text"]
        }

        json_name = file_name + ".json"
        json_path = os.path.join(output_folder, json_name)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Saved: {json_name}")

print("All files completed.")