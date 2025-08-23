from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def find_expensive_element(money):
    shop= {}
    prices=[]
    elements= driver.find_elements(By.CSS_SELECTOR, "#store > div b")
    for element in elements:
        element_list= element.text.split(" - ")
        if len(element_list) == 2:
            shop[element]= int(element_list[1].replace(",",""))
            prices.append(int(element_list[1].replace(",","")))
        #print(shop)

    affordable = {k: v for k, v in shop.items() if v <= money}
    if not affordable:
        return None
    else: 
        return max(affordable.keys(), key= affordable.get)


driver= webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

try:
    driver.find_element(By.CSS_SELECTOR, "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button > p").click()
except:
    print("There is not consent page")

cookie= driver.find_element(By.ID, "cookie")
print(cookie)

while True:
    start_time= time.time()
    while time.time()-start_time <= 5:
        cookie.click()

    money= driver.find_element(By.ID, "money").text
    buy= find_expensive_element(int(money))
    if buy:
        buy.click()
    



