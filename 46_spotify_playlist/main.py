import requests
from bs4 import BeautifulSoup
import lxml
import pathlib
CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

ENDPOINT= "https://www.billboard.com/charts/hot-100/"
date = input("Enter the date in YYYY-MM-DD format: ")
response = requests.get(ENDPOINT + date + "/")
response.raise_for_status()  # Check if the request was successful
soup = BeautifulSoup(response.text, "lxml")


songs = [song.getText().replace("\n","").replace("\t","") for song in soup.select(selector= "li > #title-of-a-story")]

print(len(songs))


with open(CURRENT_DIR / f"{date} top 100.txt", "w") as file:
    for index, song in enumerate(songs):
        file.write(f"{index+1}) {song}\n")