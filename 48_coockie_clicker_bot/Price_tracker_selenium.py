from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # With this version of selenium you don't need to specify the path of the driver
print(driver.capabilities["browserName"])
print(driver.capabilities["browserVersion"])

driver.get("https://www.amazon.es/Cecotec-Multifunci%C3%B3n-Funciones-Recetario-Integrado/dp/B0BGSRV33C/ref=sr_1_1_sspa?crid=1T2PAAJE2HGDJ&dib=eyJ2IjoiMSJ9.cIBOs0sD0tkesJa4w_BQYdvijrFgWTW95HUEPViFFb6I7HMBF7KSvdkdkP01VWmsezR7DuOFhvhiMfhgVndw9EHt7XTG_JK996g7ZnCOhFHpyJGnVwf38udXD9I6mU1ImdKq4a842X9Xyltsj9gaqrPikWvGPiLDIlWv0CQEQsqz-zAB7PTaSjr3-nkAYo0EDsGcBcZCfGOwVRq6bldFDnaQhIKgYpjwXus582NrQRZhN9Qa-OTSm8Q4ZPM_S_i2R2SeugFFzIj1uuIOo1sy26e-SVccXzTUDEzm6DmU2O8.1aIx4gSUYhP1_jhMLEf0v0ewk01OPX5mWGgTa0k0O18&dib_tag=se&keywords=thermomix&qid=1755679777&sprefix=thermo%2Caps%2C117&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
driver.implicitly_wait(3) 
buttons = driver.find_elements(By.CLASS_NAME, "a-button-text")

if buttons:  # lista no vacía
    buttons[0].click()
    print("Button clicked")
else:
    print("The button was not found")


driver.implicitly_wait(5) #wait 5 seconds to load the page

int_price= int(driver.find_element(By.CLASS_NAME, "a-price-whole").text.replace(".",""))
fractional_price= int(driver.find_element(By.CLASS_NAME, "a-price-fraction").text.replace(".",""))
print(f"Price: {int_price}.{fractional_price}")

##Other functionalities
image= driver.find_element(By.CSS_SELECTOR, "img#landingImage")
print(image.size)

searcher= driver.find_element(By.NAME, "field-keywords")
print(searcher.tag_name)
searcher.clear()
searcher.send_keys("Rtx 4060ti")
searcher.submit()
driver.implicitly_wait(5)

x_path= '//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[1]/a'
link= driver.find_element(By.XPATH, x_path)

href= link.get_attribute("href")
driver.get(href)
driver.implicitly_wait(5)
driver.quit() #quit close the browser and close closes the tabç
