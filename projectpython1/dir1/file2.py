from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#sel=Select(driver.find_element_by_xpath("//input[@name='exp']")
driver.find_element_by_xpath("//input[@value='2']").click()