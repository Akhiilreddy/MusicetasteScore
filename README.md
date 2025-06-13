# 🎧 Spotify Playlist Taste Matcher

This app lets two users compare their Spotify playlists to see how similar their music tastes are. It fetches metadata, downloads representative audio tracks from YouTube, extracts audio features, and computes a similarity score using FAISS with HNSW indexing.

---

## 🚀 Features

- 🎵 Accepts two Spotify playlist links
- 📥 Fetches metadata using Spotify Web API
- 🔊 Downloads audio clips from YouTube
- 🎼 Extracts MFCC audio features with Librosa
- ⚡ Computes playlist similarity using FAISS HNSW
- 📊 Displays match score with a color-coded bar
- 💬 Shows a personalized match message

---

## 📦 Tech Stack

| Component        | Tool/Library         | Description                                 |
|------------------|----------------------|---------------------------------------------|
| UI               | Streamlit            | Web interface                               |
| Metadata         | Spotipy              | Spotify playlist and track metadata         |
| Audio Download   | yt-dlp               | Downloads best audio match from YouTube     |
| Feature Extract  | Librosa              | Extracts MFCCs from WAV audio               |
| Similarity       | FAISS (HNSW)         | Fast Approximate Nearest Neighbor Search    |
| Plotting         | Matplotlib           | Horizontal similarity bar                   |

---

## 🔬 About FAISS HNSW

This project uses **FAISS (Facebook AI Similarity Search)** with **HNSW (Hierarchical Navigable Small World graphs)** to compute similarity between playlists. Each song is converted into a vector using MFCCs, and HNSW indexing allows fast and efficient nearest-neighbor search across song vectors.

---

## 📁 Project Structure
musictaste/
├── app.py # Main Streamlit app
├── spotify_metadata.py # Fetches playlist metadata
├── download_audio.py # Downloads audio from YouTube
├── extract_features.py # Extracts MFCC features
├── match_user.py # Computes HNSW simila# 🎧 Spotify Playlist Taste Matcher

This project compares the musical tastes of two users based on their Spotify playlists. It analyzes audio features from songs and calculates a similarity score using FAISS with HNSW (Hierarchical Navigable Small World) indexing.

---

## 🔍 What It Does

- Accepts **two Spotify playlist links**
- Fetches track metadata using the **Spotify Web API**
- Searches and downloads audio samples from **YouTube**
- Extracts audio features like **MFCCs** using **Librosa**
- Computes similarity using **FAISS HNSW** nearest neighbor search
- Displays a **percentage similarity**, a **color bar**, and a **custom message**

---

## 🧠 How It Works

1. **Playlist Parsing**  
   Uses `spotipy` to extract track names and artist names.

2. **Audio Downloading**  
   Searches YouTube using `yt-dlp` and downloads the best audio match for each track.

3. **Feature Extraction**  
   Converts each audio track to a `.wav` and extracts **Mel-frequency cepstral coefficients (MFCCs)** using `librosa`.

4. **Similarity Matching (HNSW)**  
   Uses **Facebook's FAISS library** with the **HNSW algorithm** to compare feature vectors efficiently:
   - One playlist is indexed
   - The second is queried against it
   - Distance is averaged and inverted into a similarity score

5. **Visualization**  
   Shows a color-coded bar from **red to green** and a message based on similarity score.

---

## 🧪 Key Technologies

| Feature           | Tool / Library      |
|-------------------|---------------------|
| UI                | Streamlit           |
| Spotify API       | Spotipy             |
| Audio Download    | yt-dlp              |
| Audio Conversion  | pydub (FFmpeg)      |
| Feature Extraction| Librosa             |
| Similarity Search | FAISS (HNSW Index)  |
| Plotting          | Matplotlib          |

---

## 📁 Project Structure

musictaste/
├── app.py # Main Streamlit interface
├── spotify_metadata.py # Spotify metadata fetching
├── download_audio.py # YouTube search + download
├── extract_features.py # MFCC feature extraction
├── match_user.py # FAISS HNSW-based similarity
├── audio/ # Downloaded audio
├── data/ # Playlist metadata in JSON
├── requirements.txt # Python dependencies


2. Set Up Environment
bash
Copy code
python -m venv matcher-env
matcher-env\Scripts\activate  # Windows
#or
source matcher-env/bin/activate  # Mac/Linux



3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Make sure you have ffmpeg installed and added to PATH.


4. Add Your Spotify API Credentials
Create a file named config.py:

python
Copy code
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"
REDIRECT_URI = "http://localhost:8888/callback"

5. Run the App
bash
Copy code
streamlit run app.py




🛠️ Scope for Improvement
✅ Improve error handling and show skipped tracks
🎧 Cache processed playlists to avoid re-downloading
💡 Add genre-level or tempo-based comparison
🎶 Visualize overlapping and unique tracks
🌍 Add language/region awareness for multicultural playlists
📈 Deploy on Streamlit Cloud or containerize via Docker



🤝 Contributions & Collaborations
Contributions are welcome! Whether it's cleaning code, adding new audio features, improving UI, or exploring new ML models — feel free to open issues or submit a pull request.
💬 Also open to collaborating on music analytics, embeddings, and similarity learning projects — let’s build something impactful!
