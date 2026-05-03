# 🎥 AI Video Transcription & Word Frequency Analyzer

A Python-based application that extracts audio from video, transcribes speech into text using AI, and analyzes the frequency of user-defined words through an interactive UI.

---

## 🚀 Features

* 🎬 Extract audio from video files
* 🧠 Convert speech to text using OpenAI Whisper
* 🔍 Count frequency of user-defined words (case-insensitive)
* 🧹 Handle punctuation using regex for accurate counting
* 🌐 Interactive UI built with Streamlit

---

## 🧠 How It Works

1. Input video (.mp4)
2. Audio extraction using FFmpeg → converts to `.wav`
3. Transcription using Whisper → converts audio to text
4. Text processing using regex → cleans and normalizes text
5. Word frequency analysis → counts occurrences of target word

---

## 🛠️ Tech Stack

* Python
* FFmpeg (audio extraction)
* OpenAI Whisper (speech-to-text)
* Streamlit (UI)
* Regex (`re` module)

---

## 📁 Project Structure

```
video-word-frequency-analyzer/
│
├── app/
│   ├── main.py
│   ├── ui.py
│   ├── audio.py
│   ├── Trans.py
│   ├── counter.py
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/video-word-frequency-analyzer.git
cd video-word-frequency-analyzer
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Install FFmpeg

Download FFmpeg and add it to your system PATH.

---

## ▶️ Run the Project

### 🔹 Option 1: CLI Mode

```
python app/main.py
```

---

### 🔹 Option 2: Streamlit UI (Recommended)

```
python -m streamlit run app/ui.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 📊 Example Output

```
Transcription:
so I was thinking so maybe so yeah

Count of "so": 3
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

Developed during a Python Developer Internship to explore audio processing, AI transcription, and full-stack application development.

---

## ⭐ Support

If you found this useful, give it a star ⭐ on GitHub!
