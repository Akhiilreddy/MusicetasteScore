import streamlit as st
import os, shutil
import json
from spotify_metadata import fetch_metadata_from_playlist
from download_audio import download_tracks_from_metadata
from extract_features import extract_all_features
from match_user import match_playlists_similarity
import matplotlib.pyplot as plt

# ----------------------------
def clear_old_data():
    for folder in ["audio/user1", "audio/user2", "data"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)

# ----------------------------
def show_similarity_bar(score):
    fig, ax = plt.subplots(figsize=(6, 1.2))
    cmap = plt.get_cmap("RdYlGn")
    color = cmap(score / 100)

    ax.barh([0], [score], color=color, height=0.5)
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_yticks([])
    ax.set_title("🎧 Music Taste Similarity", fontsize=14)
    st.pyplot(fig)

# ----------------------------
def get_message(score):
    if score > 90:
        return "🎉 You both vibe perfectly! A musical match made in heaven."
    elif score > 75:
        return "🥳 Great sync! Most of your music choices align well."
    elif score > 50:
        return "🎶 Decent overlap. You've got some songs in common!"
    elif score > 30:
        return "🔍 There's some musical chemistry, but tastes diverge a bit."
    else:
        return "😅 Opposites attract? Your playlists are from different planets."

# ----------------------------
def process_and_match(url1, url2):
    clear_old_data()

    # Fetch metadata
    metadata1 = fetch_metadata_from_playlist(url1, "data/metadata1.json")
    metadata2 = fetch_metadata_from_playlist(url2, "data/metadata2.json")

    # Download audio
    download_tracks_from_metadata(metadata1, "audio/user1")
    download_tracks_from_metadata(metadata2, "audio/user2")

    # Extract features
    feats1 = extract_all_features("audio/user1")
    feats2 = extract_all_features("audio/user2")

    # Compute similarity
    score = match_playlists_similarity(feats1, feats2)
    return round(score, 2), get_message(score)

# ----------------------------
# Streamlit UI
import streamlit as st
import os, shutil
import json
from spotify_metadata import fetch_metadata_from_playlist
from download_audio import download_tracks_from_metadata
from extract_features import extract_all_features
from match_user import match_playlists_similarity
import matplotlib.pyplot as plt

# ----------------------------
def clear_old_data():
    for folder in ["audio/user1", "audio/user2", "data"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)

# ----------------------------
def show_similarity_bar(score):
    fig, ax = plt.subplots(figsize=(6, 1.2))
    cmap = plt.get_cmap("RdYlGn")
    color = cmap(score / 100)

    ax.barh([0], [score], color=color, height=0.5)
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_yticks([])
    ax.set_title("🎧 Music Taste Similarity", fontsize=14)
    st.pyplot(fig)

# ----------------------------
def get_message(score):
    if score > 90:
        return "🎉 You both vibe perfectly! A musical match made in heaven."
    elif score > 75:
        return "🥳 Great sync! Most of your music choices align well."
    elif score > 50:
        return "🎶 Decent overlap. You've got some songs in common!"
    elif score > 30:
        return "🔍 There's some musical chemistry, but tastes diverge a bit."
    else:
        return "😅 Opposites attract? Your playlists are from different planets."

# ----------------------------
def process_and_match(url1, url2):
    clear_old_data()

    # Fetch metadata
    metadata1 = fetch_metadata_from_playlist(url1, "data/metadata1.json")
    metadata2 = fetch_metadata_from_playlist(url2, "data/metadata2.json")

    # Download audio
    download_tracks_from_metadata(metadata1, "audio/user1")
    download_tracks_from_metadata(metadata2, "audio/user2")

    # Extract features
    feats1 = extract_all_features("audio/user1")
    feats2 = extract_all_features("audio/user2")

    # Compute similarity
    score = match_playlists_similarity(feats1, feats2)
    return round(score, 2), get_message(score)

# ----------------------------
# Streamlit UI
st.set_page_config(page_title="Spotify Playlist Matcher", page_icon="🎶")
st.title("🎵 Couple Music Taste Matcher")
st.markdown("Compare two Spotify playlists and find out how close your music tastes are!")

url1 = st.text_input("🎧 Paste User 1's Spotify Playlist URL")
url2 = st.text_input("🎧 Paste User 2's Spotify Playlist URL")

if st.button("Match Music Taste", key="match_button"):
    if not url1 or not url2:
        st.warning("⚠️ Please provide both playlist URLs.")
    else:
        with st.spinner("🎼 Processing playlists..."):
            try:
                score, message = process_and_match(url1, url2)
                show_similarity_bar(score)
                st.markdown(f"## 🎯 Similarity Score: **{score:.2f}%**")
                st.markdown(f"### {message}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
