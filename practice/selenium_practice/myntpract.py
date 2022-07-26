from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver= webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.switch_to.new_window()
driver.get("https://www.myntra.com/shop/women")
time.sleep(5)
#driver.switch_to.alert().dismiss()
action=ActionChains(driver)
women=driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/nav/div/div[2]/div/a")
action.move_to_element(women).perform()
