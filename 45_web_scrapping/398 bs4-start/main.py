
import pathlib
from bs4 import BeautifulSoup
import lxml

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

with open(CURRENT_DIR / "website.html",mode="r") as f:
    content = f.read()
print(content)
soup = BeautifulSoup(content, "lxml")
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.h1)
print(soup.find_all("h1"))
all_a_tags = soup.find_all("a")
print(all_a_tags)
for tag in all_a_tags:
    print(tag.getText())
    print(tag.get("href"))
print(soup.find(id="name"))
print(soup.find(class_="heading"))
print(soup.select_one("p a"))
print(soup.select(selector= "#name"))
print(soup.select(selector= ".heading"))