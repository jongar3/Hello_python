from bs4 import BeautifulSoup
import requests
import lxml
import pyperclip 
URL= "https://news.ycombinator.com/"
response= requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())
pyperclip.copy(soup.prettify())

titulos = [a.get_text() for a in soup.select("span.titleline > a")]


for (i, titulo) in enumerate(titulos):
    print(f"{i+1}. {titulo}")
