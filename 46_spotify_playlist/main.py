import requests
from bs4 import BeautifulSoup
import lxml
import os
import pathlib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

ENDPOINT= "https://www.billboard.com/charts/hot-100/"
date = input("Enter the date in YYYY-MM-DD format: ")
response = requests.get(ENDPOINT + date + "/")
response.raise_for_status()  # Check if the request was successful
soup = BeautifulSoup(response.text, "lxml")


songs = [song.getText().replace("\n","").replace("\t","") for song in soup.select(selector= "li > #title-of-a-story")]

print(len(songs))

name_title= f"{date} top 100.txt"
with open(CURRENT_DIR / name_title, "w") as file:
    for index, song in enumerate(songs):
        file.write(f"{index+1}) {song}\n")

##CREATE SPOTIFY PLAYLIST
load_dotenv()  # Load environment variables from .env file

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
if not client_id or not client_secret:
    raise ValueError("client_id and client_secret must be set in a local .env file")
print(client_id)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public"
))

# Obtener usuario
user_id = sp.current_user()["id"]

# Crear playlist
playlist = sp.user_playlist_create(user=user_id, name=name_title, public=True)
playlist_id = playlist["id"]

# Use sp.search to try to find the song and add it to the playlist
for song in songs:    
    results = sp.search(q=song, type="track", limit=1)

    if results["tracks"]["items"]:
        track_uri = results["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id, [track_uri])
        print("Added:", results["tracks"]["items"][0]["name"], "-", results["tracks"]["items"][0]["artists"][0]["name"])
    else:
        print(f"Song '{song}' not found on Spotify, skipping...")