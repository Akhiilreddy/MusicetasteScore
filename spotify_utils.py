
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private playlist-read-collaborative"
))

def extract_id(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]

def get_track_list(playlist_url, user_tag):
    playlist_id = extract_id(playlist_url)
    results = sp.playlist_tracks(playlist_id)
    return [item["track"]["name"] + " " + item["track"]["artists"][0]["name"] for item in results["items"]]
