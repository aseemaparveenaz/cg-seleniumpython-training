from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
action=ActionChains(driver)
ele=driver.find_element_by_name("firstname")
action.click(ele)
action.send_keys("aseema")
action.context_click(ele)
time.sleep(3)
driver.implicitly_wait(7)
driver.execute_script("window.open('about:blank' , 'secondtab');")
time.sleep(6)
driver.switch_to.window("secondtab")
driver.get("http://sahitest.com/demo/clicks.htm")
ele1=driver.find_element_by_xpath('//input[@value="right click me"]')
action=ActionChains(driver)
action.context_click(ele1).send_keys(Keys.ARROW_DOWN).perform()