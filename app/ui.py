import os
import tempfile
from collections import Counter

import streamlit as st
from supabase import create_client, Client
 
import os

os.environ["PATH"] += os.pathsep + r"C:\Users\vedik\Downloads\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"
# Optional Whisper import
try:
    import whisper
except ImportError:
    whisper = None


st.set_page_config(
    page_title="AI Video Transcription Analyzer",
    page_icon="🎙️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FDE2E4 0%, #E2ECE9 50%, #DDE7F0 100%);
}

.block-container {
    max-width: 720px;
    padding-top: 3rem;
    padding-bottom: 2rem;
}

.auth-card, .dashboard-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(10px);
    padding: 2rem 2.2rem;
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.6);
    margin-bottom: 1.5rem;
}

.auth-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    color: #334155;
    margin-bottom: 0.4rem;
}

.auth-subtitle {
    text-align: center;
    color: #64748B;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}

.stTextInput > div > div > input {
    border-radius: 12px;
    border: 1px solid #CBD5E1;
    padding: 0.75rem 1rem;
    background-color: #FFFFFF;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    padding: 0.75rem;
    font-weight: 600;
    font-size: 0.95rem;
    background: linear-gradient(90deg, #A7C7E7, #CDB4DB);
    color: #1E293B;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #CDB4DB, #A7C7E7);
    color: #0F172A;
    transform: translateY(-1px);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    justify-content: center;
    margin-bottom: 1rem;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 8px 20px;
    background-color: rgba(255,255,255,0.5);
    color: #475569;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background-color: white !important;
    color: #334155 !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

#MainMenu, footer, header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_word_frequency(text, top_n=15):
    words = text.lower().replace(".", "").replace(",", "").split()

    stop_words = {
        "the", "is", "am", "are", "was", "were", "a", "an", "and", "or",
        "to", "of", "in", "on", "for", "with", "this", "that", "it", "as",
        "at", "by", "from", "be", "been", "have", "has", "had", "i", "you",
        "we", "they", "he", "she", "my", "your", "our", "their", "his", "her", "its", "what", "who", "which", "when", "where", "why", "how", "all", "any", "do", "does", "did", "not", "but", "if", "so", "up", "out", "about", "into", "over", "after", "before", "between", "under", "again", "further", "then", "once"
    }

    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    return Counter(filtered_words).most_common(top_n)


def dashboard():
    st.markdown("""
    <div class="dashboard-card">
        <div class="auth-title">🎙️ AI Video Transcription Dashboard</div>
        <div class="auth-subtitle">
            Upload your video/audio file, generate transcript, and analyze frequently used words.
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload video/audio file",
        type=["mp4", "mov", "mkv", "avi", "mp3", "wav", "m4a"]
    )

    if uploaded_file:
        file_size_mb = uploaded_file.size / (1024 * 1024)
        st.success(f"Uploaded: {uploaded_file.name}")
        st.info(f"File size: {file_size_mb:.2f} MB")

        if file_size_mb > 5120:
            st.error("File is larger than 5 GB. Please upload a smaller file.")
            return

        if st.button("Generate Transcript"):
            if whisper is None:
                st.error("Whisper is not installed. Run: pip install openai-whisper")
                return

            with st.spinner("Transcribing... This may take time for large files."):
                suffix = os.path.splitext(uploaded_file.name)[1]

                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_path = temp_file.name

                try:
                    model = whisper.load_model("base")
                    result = model.transcribe(temp_path)
                    transcript = result["text"]

                    st.subheader("📝 Generated Transcript")
                    st.text_area("Transcript", transcript, height=250)

                    st.download_button(
                        "Download Transcript",
                        transcript,
                        file_name="transcript.txt",
                        mime="text/plain"
                    )

                    st.subheader("📊 Top Frequent Words")
                    word_freq = get_word_frequency(transcript)

                    if word_freq:
                        for word, count in word_freq:
                            st.write(f"**{word}** : {count}")
                    else:
                        st.warning("No meaningful words found for analysis.")

                except Exception as e:
                    st.error(f"Transcription failed: {e}")

                finally:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

    st.markdown("---")

    if st.button("Logout"):
        del st.session_state["user"]
        st.rerun()


if "user" in st.session_state:
    dashboard()
    st.stop()


st.markdown("""
<div class="auth-card">
    <div class="auth-title">🎙️ AI Video Transcription Analyzer</div>
    <div class="auth-subtitle">
        Login or create an account to transcribe videos and analyze frequently used words.
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔐 Login", "✨ Sign Up"])

with tab1:
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if response.user:
                st.session_state["user"] = response.user
                st.success("Login successful! 🎉")
                st.rerun()
            else:
                st.error("Invalid email or password.")

        except Exception as e:
            st.error(f"Login failed: {e}")

with tab2:
    signup_email = st.text_input("Email", key="signup_email")
    signup_password = st.text_input("Password", type="password", key="signup_password")

    if st.button("Create Account", key="signup_btn"):
        try:
            response = supabase.auth.sign_up({
                "email": signup_email,
                "password": signup_password
            })

            if response.user:
                st.success("Account created! Please check your email and verify before login.")
            else:
                st.warning("Signup request sent. Please check your email.")

        except Exception as e:
            error_msg = str(e).lower()

            if "rate limit" in error_msg:
                st.warning("Too many signup attempts. Please wait before trying again.")
            elif "email signups are disabled" in error_msg:
                st.error("Email signup is disabled in Supabase.")
            else:
                st.error(f"Sign up failed: {e}")

st.markdown("""
<div style="text-align:center; margin-top:20px; color:#64748B; font-size:13px;">
    Built  using Streamlit, Supabase, and OpenAI Whisper
</div>
""", unsafe_allow_html=True)