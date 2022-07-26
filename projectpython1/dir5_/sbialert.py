from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://retail.onlinesbi.com/retail/login.htm#")
driver.find_element_by_link_text("CONTINUE TO LOGIN").click()
driver.find_element_by_partial_link_text("New User ?").click()
time.sleep(2)
driver.switch_to.alert.dismiss()