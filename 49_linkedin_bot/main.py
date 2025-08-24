from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

driver= webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4289763064&keywords=Desarrollador%20de%20Python&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

driver.find_element(By.CSS_SELECTOR, "#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button").click()

load_dotenv()
email= os.getenv("email")
password= os.getenv("password")
print(password)

email_input= driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal_session_key")
email_input.send_keys(email)
password_input= driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_input.send_keys(password)

sign_up_button=driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal > div > section > div > div > form > div.flex.justify-between.sign-in-form__footer--full-width > button")
sign_up_button.click()

lista= driver.find_elements(By.CSS_SELECTOR, "a.job-card-container__link")

for element in lista[0::2]:
    element.click()
    print(element.text)
    save_button= driver.find_element(By.CLASS_NAME, "jobs-save-button__text")
    save_button.click() #Saves the current JOB in python development