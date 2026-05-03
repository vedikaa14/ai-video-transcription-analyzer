import os
import streamlit as st

from main import process

# Fix FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg\bin"

# Create data folder if missing
os.makedirs("data", exist_ok=True)

st.title("🎥 Video Word Frequency Analyzer")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])
word = st.text_input("Enter word to count", "so")

if uploaded_file is not None:
    video_path = f"data/{uploaded_file.name}"

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Video uploaded successfully!")

    if st.button("Process Video"):
        if not word.strip():
            st.error("Please enter a word to count.")
        else:
            with st.spinner("⏳ Processing video..."):
                text, count = process(video_path, word.strip())

            st.success("✅ Processing completed!")

            st.subheader("📄 Transcription")
            st.write(text)

            st.subheader(f"🔢 Count of '{word}'")
            st.success(count)