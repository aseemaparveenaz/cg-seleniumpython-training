from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
dragger = driver.find_element_by_id("dragger") # dragged elements
item1 = driver.find_element_by_xpath("//div[text()='Item 1']") #targets element 1
item2 = driver.find_element_by_xpath("//div[text()='Item 2']") #targets element 2
item3 = driver.find_element_by_xpath("//div[text()='Item 3']") #targets element 3
item4 = driver.find_element_by_xpath("//div[text()='Item 4']") #targets element 4
action = ActionChains(driver)
action.drag_and_drop(dragger, item1).perform() #1.mobile dragger to the target 1
sleep(2)
action = ActionChains(driver)
action.click_and_hold(dragger).release(item2).perform()
sleep(20)
action = ActionChains(driver)
action.click_and_hold(dragger).move_to_element(item3).release().perform()
sleep(2)
#action.drag_and_drop_by_offset(dragger, 400, 150).perform()
action = ActionChains(driver)
action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()
sleep(2)
driver.quit()