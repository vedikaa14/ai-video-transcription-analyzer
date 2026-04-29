# 🎥 Video Word Frequency Analyzer

A Python-based pipeline that extracts audio from a video, transcribes it into text, and analyzes the frequency of specific words (e.g., "so").

---

## 🚀 Features

* 🎬 Extract audio from video files
* 🧠 Convert speech to text using AI
* 🔍 Count frequency of specific words (case-insensitive)
* 🧹 Handles punctuation using regex for accurate counting

---

## 🧠 How It Works

1. **Input Video** (`.mp4`)
2. **Audio Extraction** → Converts video to `.wav`
3. **Transcription** → Converts audio to text
4. **Text Processing** → Cleans and splits words
5. **Word Count** → Counts occurrences of target word

---

## 🛠️ Tech Stack

* Python
* FFmpeg (for audio extraction)
* OpenAI Whisper (for speech-to-text)
* Regex (`re` module) for text processing

---

## 📁 Project Structure

```
video-word-frequency-analyzer/
│
├── app/
│   ├── main.py
│   ├── audio.py
│   ├── Trans.py
│   ├── counter.py
│
├── data/
│   └── input.mp4
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/video-word-frequency-analyzer.git
cd video-word-frequency-analyzer
```

---

### 2. Install dependencies

```
pip install openai-whisper
```

---

### 3. Install FFmpeg

* Download FFmpeg
* Add it to your system PATH
  OR
* Use full path in code

---

### 4. Add your video

Place your video file in the `data/` folder:

```
data/input.mp4
```

---

### 5. Run the project

```
python app/main.py
```

---

## 📊 Example Output

```
--- RESULT ---

--- RAW TRANSCRIPTION ---
so I was thinking so maybe so yeah
------------------------

Count of 'so': 3
```

---

## ⚠️ Notes

* First run may take time (model download)
* Accuracy depends on audio quality
* Filler words like "so", "um" may sometimes be missed

---

## 🚀 Future Improvements

* CLI input for custom files and words
* Web interface (Streamlit / Flask)
* Support multiple word analysis
* Improved accuracy with larger models

---

## 💡 Use Cases

* Speech analysis (filler words detection)
* Interview feedback tools
* Content analysis for videos
* Meeting transcription insights

---

## 👨‍💻 Author

Built as a hands-on project to explore audio processing, AI transcription, and text analysis.

---

## ⭐ If you found this useful

Give it a star ⭐ on GitHub!
