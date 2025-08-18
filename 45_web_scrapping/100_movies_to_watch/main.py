import requests
from bs4 import BeautifulSoup
import pathlib
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
CURRENT_DIR = pathlib.Path(__file__).parent.resolve()


response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
titles= soup.select("h3.title")
#titles.reverse() works too, equivalent to title[::-1]
titles=list(titles)
films_string=""
for (i,title) in enumerate(reversed(titles)):
    title_text = title.get_text()
 
    if ") " in title_text:
        name= title_text.split(") ")[1]  # Extracting the title after the number
    #print(f"{i+1}. {name}")  
    films_string += f"{i+1}. {name}\n"

print(films_string)

with open(CURRENT_DIR / "movies.txt", "w") as file:
    file.write(films_string)