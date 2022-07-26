from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://naukri.com")
time.sleep(5)

companies = driver.find_elements_by_class_name("mTxt")
# Object of ActionChains
action1 = ActionChains(driver)
action1.move_to_element(companies[2])
action1.perform()

driver.find_element_by_link_text("Interview Questions").click()