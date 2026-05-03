# 🎥 AI Video Transcription & Word Frequency Analyzer

A Python-based application that extracts audio from video, transcribes speech using AI, and analyzes the frequency of specific words (e.g., "so") through an interactive pipeline.

---

## 🚀 Features

* 🎬 Extract audio from video files
* 🧠 Convert speech to text using AI
* 🔍 Count frequency of user-defined words (case-insensitive)
* 🧹 Handle punctuation using regex for accurate analysis
* 💻 Interactive UI using Streamlit

---

## 🧠 How It Works

1. **Input Video** (`.mp4`)
2. **Audio Extraction** → Converts video to `.wav` using FFmpeg
3. **Transcription** → Converts audio to text using Whisper
4. **Text Processing** → Cleans and splits words using regex
5. **Word Analysis** → Counts occurrences of target word

---

## 🛠️ Tech Stack

* Python
* FFmpeg (audio extraction)
* OpenAI Whisper (speech-to-text)
* Streamlit (UI)
* Regex (`re` module) for text processing

---

## 📁 Project Structure

```id="0bcz3a"
video-word-frequency-analyzer/
│
├── app/
│   ├── main.py
│   ├── ui.py
│   ├── audio.py
│   ├── Trans.py
│   ├── counter.py
│
├── data/
│   └── input.mp4
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```id="3e3p7r"
git clone https://github.com/your-username/video-word-frequency-analyzer.git
cd video-word-frequency-analyzer
```

---

### 2. Install dependencies

```id="r7kpxg"
pip install -r requirements.txt
```

---

### 3. Install FFmpeg

* Download FFmpeg
* Add it to your system PATH

---

### 4. Run the application

#### ▶️ CLI version

```id="jz36cv"
python app/main.py
```

#### ▶️ UI version (recommended)

```id="0u3nbz"
python -m streamlit run app/ui.py
```

---

## 📊 Example Output

```id="q2h7dl"
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

* Support multiple word analysis
* Highlight words in transcription
* Add timestamps for detected words
* Deploy application publicly

---

## 💡 Use Cases

* Speech analysis (filler word detection)
* Interview feedback tools
* Content analysis for videos
* Meeting transcription insights

---

## 👨‍💻 Author

Developed during a Python Developer Internship to explore audio processing, AI transcription, and text analysis.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
