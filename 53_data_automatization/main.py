from bs4 import BeautifulSoup
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_DIR = pathlib.Path(__file__).resolve().parent

ZILLOW_LINK="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.926019038457014%2C%22south%22%3A37.65851126658599%2C%22east%22%3A-122.21531955126953%2C%22west%22%3A-122.60121432666016%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22personalizedsort%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A595457%7D%7D%2C%22isListVisible%22%3Atrue%2C%22listPriceActive%22%3Atrue%2C%22category%22%3A%22cat1%22%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
GOOGLE_FORMS_LINK="https://docs.google.com/forms/d/e/1FAIpQLSd7eP_4sUaFrnJZgX6tmIbZSTKDpObYtzTCnssj8PDiLBUJqA/viewform?usp=dialog"

with open(BASE_DIR / "zillow_local.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "lxml")

price_list=[]
price_list_no_formatted=[]
price_objects= soup.select("div .PropertyCardWrapper__StyledPriceGridContainer-srp-8-109-3__sc-16e8gqd-0 > .PropertyCardWrapper__StyledPriceLine-srp-8-109-3__sc-16e8gqd-1")

#GET THE PRICE LIST
for price_object in price_objects:
    price_list_no_formatted.append(price_object.get_text())
    
for price_no_formatted in price_list_no_formatted:
    price=""
    for letter in price_no_formatted:
        if letter.isdigit():
                price+= letter
    
    if len(price)>=5:
        price=price[0:-1]
    if price:
        price_list.append(price)

#GET ADDRESS

address_list=[]
address_objects= soup.select("address")

for address_object in address_objects:
    address_list.append(address_object.get_text().strip())
print(address_list)

links_list=[]
links_list_rep=[]
links_objects_norep=[]
links_objects= soup.select("div.StyledPhotoCarouselSlide-c11n-8-109-3__sc-jwte3-0 > a.Anchor-c11n-8-109-3__sc-hn4bge-0")


for links_object in links_objects:
    links_list_rep.append(links_object["href"])


for elem in links_list_rep:
    if elem not in links_list:
        links_list.append(elem)


links_list= [link if "https://" in link else "https://www.zillow.com"+ link  for link in links_list]
print(links_list)


#SEND THE GOOGLE FORMS WITH SELENIUM 

driver= webdriver.Chrome()
driver.get(GOOGLE_FORMS_LINK) 
for (price, address, link) in zip(price_list, address_list, links_list):
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd")))
    inputs[0].click()
    inputs[0].send_keys(address)
    inputs[1].send_keys("$"+price)
    inputs[2].send_keys(link)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    driver.find_element(By.CSS_SELECTOR, "a").click()
    del inputs
    time.sleep(2)
   
driver.quit()