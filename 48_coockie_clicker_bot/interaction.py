from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome() # With this version of selenium you don't need to specify the path of the driver

driver.get("https://en.wikipedia.org/wiki/Main_Page")

css_selector="#articlecount > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)"


def find(driver, by, value, timeout=10, clickable=False):
    """Find an element on the page with explicit wait."""
    wait = WebDriverWait(driver, timeout)
    if clickable:
        return wait.until(EC.element_to_be_clickable((by, value)))
    else:
        return wait.until(EC.presence_of_element_located((by, value)))


number_articles=driver.find_element(By.CSS_SELECTOR, css_selector).text
print(f"Number of articles in Wikipedia: {number_articles}")

driver.find_element(By.LINK_TEXT, "Wikipedia").click()
driver.find_element(By.CSS_SELECTOR, "#p-search > a").click()
driver.implicitly_wait(3) 
searcher = find(driver, By.NAME, "search")

print(searcher.tag_name)
searcher = find(driver, By.NAME, "search")
searcher.clear()
searcher = find(driver, By.NAME, "search")
searcher.send_keys("Python")
searcher = find(driver, By.NAME, "search") #Every time you interact with an element you have to find it again The page ""reloads""
searcher.submit()
driver.quit()







