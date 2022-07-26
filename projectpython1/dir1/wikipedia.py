from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
try:
    driver.get("https://en.wikipedia.org")
    print(driver.title)
    input=driver.find_element_by_id("searchInput")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.ID,"content")))
    print(driver.title)
    time.sleep(20)
finally:
    print("hello")