from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.softwaretestingmaterial.com/")
l=driver.find_element_by_link_text("Tutorials")
act=ActionChains(driver)
act.move_to_element(l)
act.perform()