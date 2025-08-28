from bs4 import BeautifulSoup
import requests
import os 
from dotenv import load_dotenv
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

ZILLOW_LINK="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.926019038457014%2C%22south%22%3A37.65851126658599%2C%22east%22%3A-122.21531955126953%2C%22west%22%3A-122.60121432666016%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22personalizedsort%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A595457%7D%7D%2C%22isListVisible%22%3Atrue%2C%22listPriceActive%22%3Atrue%2C%22category%22%3A%22cat1%22%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
GOOGLE_FORMS_LINK="https://docs.google.com/forms/d/e/1FAIpQLSd7eP_4sUaFrnJZgX6tmIbZSTKDpObYtzTCnssj8PDiLBUJqA/viewform?usp=dialog"
load_dotenv()
API_KEY= os.getenv("scrapping_api_key")

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/115.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
# }
# response= requests.get(ZILLOW_LINK, headers=headers)
# response.raise_for_status()
# soup= BeautifulSoup(response.text, "lxml")
#ZILLOW BLOCKS REQUEST!

scraper_url = f"http://api.scraperapi.com?api_key={API_KEY}&url={ZILLOW_LINK}"

# Hacer la petición
response = requests.get(scraper_url)
response.raise_for_status()

# Parsear con BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())
archivo_html = "zillow_local.html"

# Guardar el HTML en un archivo
with open(BASE_DIR / archivo_html, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"HTML saved in {archivo_html}")