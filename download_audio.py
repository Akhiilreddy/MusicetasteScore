
import os
import yt_dlp
from pydub import AudioSegment

def download_audio(track_name, artist, output_path):
    query = f"{track_name} {artist} audio"
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "outtmpl": f"{output_path}.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch1:{query}"])
            mp3_file = f"{output_path}.mp3"
            if os.path.exists(mp3_file):
                wav_file = f"{output_path}.wav"
                AudioSegment.from_mp3(mp3_file).export(wav_file, format="wav")
                os.remove(mp3_file)
                return wav_file
        except Exception as e:
            print(f"❌ Failed to download {query}: {e}")
    return None

def download_tracks_from_metadata(metadata, audio_dir):
    os.makedirs(audio_dir, exist_ok=True)
    for i, track in enumerate(metadata):
        name = track["name"]
        artist = track["artists"][0]
        output_path = os.path.join(audio_dir, f"{i}_{name}_{artist}".replace(" ", "_"))
        print(f"🔽 Downloading: {name} by {artist}")
        download_audio(name, artist, output_path)
