import subprocess
import os

def extract_audio(video_path, output_path="data/audio.wav"):
    os.makedirs("data", exist_ok=True)

    command = [
        r"C:\ffmpeg\ffmpeg\bin\ffmpeg.exe",
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        "-y",
        output_path
    ]

    subprocess.run(command)
    return output_path