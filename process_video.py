import os
import subprocess

video_folder = "videos"
audio_folder = "audios"

os.makedirs(audio_folder, exist_ok=True)

files = os.listdir(video_folder)

for file in files:
    video_path = os.path.join(video_folder, file)

    if not os.path.isfile(video_path):
        continue

    file_name = os.path.splitext(file)[0]

    output_path = os.path.join(audio_folder, file_name + ".mp3")

    print(f"Converting: {file}")

    subprocess.run([
        "ffmpeg",
        "-i", video_path,
        output_path
    ])

print("All videos converted successfully.")