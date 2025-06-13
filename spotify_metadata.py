
import re, json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private playlist-read-collaborative"
))

def extract_playlist_id(playlist_input):
    if "open.spotify.com/playlist/" in playlist_input:
        return playlist_input.split("/")[-1].split("?")[0]
    elif "spotify:playlist:" in playlist_input:
        return playlist_input.split(":")[-1]
    return playlist_input.strip()

def fetch_metadata_from_playlist(url, save_path):
    pid = extract_playlist_id(url)
    results = sp.playlist_tracks(pid)
    tracks = []
    for item in results["items"]:
        track = item["track"]
        if track:
            tracks.append({
                "name": track["name"],
                "artists": [a["name"] for a in track["artists"]]
            })
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(tracks, f, indent=2)
    return tracks
