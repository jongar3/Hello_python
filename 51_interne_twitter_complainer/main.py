from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

TEST_LINK= "https://www.speedtest.net/es"
TWITTER_LINK="https://x.com/home?lang=es"

load_dotenv()
twitter_email=os.getenv("email")
twitter_password= os.getenv("password")
phone= os.getenv("phone")
if not (twitter_email and twitter_password):
    raise ValueError("Introduce yout twitter email and password!")


driver= webdriver.Chrome()
driver.get(TEST_LINK)
wait = WebDriverWait(driver, 20)
try:
    cookie_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-reject-all-handler")))
    cookie_btn.click()
except:
    print("No Cookies pop-up")
else: 
    print("Cookies rejected")

#Start the speed test

start_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-text")))
start_btn.click()

#Keep your speed
driver.implicitly_wait(95) #finish the speed test
try:
    driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.desktop-app-prompt-modal > div > a").click()
except:
    print("The element does not exist")
down_speed= driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span").text
up_speed= driver.find_element(By.CSS_SELECTOR, "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span").text

print(f"Up: {up_speed}, Down: {down_speed}")

#LOGIN IN TWITTER

def complain_in_twitter(speed_down= 0, speed_up= 0):
    """Sign in the twitter account and complains about the internet speed"""
    driver.get(TWITTER_LINK)
    print("Entered to twitter") 
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 20) 
    
    cookies_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]')))
    cookies_btn.click()
    print("Cookies rejecter")
    print("Cookies rejecter")
    driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo > div > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a > div > span > span").click()
    print("Starting sign up")
    email_input= driver.find_element(By.NAME, "text")
    email_input.send_keys(twitter_email)
    email_input.send_keys(Keys.ENTER)
    try:
        password_input= driver.find_element(By.NAME, "password")
        password_input.send_keys(twitter_password)
        password_input.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
    except:
        pass
        phone_input= driver.find_element(By.NAME, "text")
        phone_input.send_keys(phone)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span').click()
        password_input= driver.find_element(By.NAME, "password")
        password_input.send_keys(twitter_password)
        password_input.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
   

    message_input= driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
    message=f"Puto Jazztel, tengo 600 Mb contratados y mi internet es de {speed_down} down/ {speed_up} up PEDROOOOO SANCHEZZZZZZZ!"
    message_input.send_keys(message)
    send_btn= driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span')
    send_btn.click()
    print("Tweet twitted!")


if float(up_speed) < 600 or float(down_speed) < 600:
    complain_in_twitter(speed_down= down_speed, speed_up= up_speed)
