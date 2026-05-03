import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg\bin"

from audio import extract_audio
from Trans import transcribe
from counter import count_word


def process(video_path, word):
    audio_path = extract_audio(video_path)
    text = transcribe(audio_path)
    count = count_word(text, word)

    return text, count


if __name__ == "__main__":
    video_path = input("Enter video path: ")
    word = input("Enter word to count: ")

    text, count = process(video_path, word)

    print("\n--- RESULT ---")
    print("\n--- RAW TRANSCRIPTION ---")
    print(text)
    print("------------------------")
    print(f"Count of '{word}':", count)