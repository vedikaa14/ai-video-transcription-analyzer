import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg\bin"  # Ensure ffmpeg is in the PATH

from audio import extract_audio
from Trans import transcribe
from counter import count_word


def process(video_path):
    audio_path = extract_audio(video_path)
    text = transcribe(audio_path)
    count = count_word(text, "so")

    print("\n--- RESULT ---")

    print("\n--- RAW TRANSCRIPTION ---")
    print(text)
    print("------------------------")

    print("Count of 'so':", count)


if __name__ == "__main__":
    process("data/input.mp4") #👈 Update with your video path