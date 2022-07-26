from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
parent=driver.find_element_by_xpath("//div[@class='mui-col-md-6 tutorial-content']/parent::div")
ancestor=driver.find_element_by_xpath("//div[@class='mui-col-md-6 tutorial-content']/ancestor::div")
child=driver.find_element_by_xpath("//div[@class='mui-col-md-6 tutorial-content']/child::div")
print("parent :",parent)
print("Ancestor of selenium_automation_practice :",ancestor)
print("child of selenium_automation_practice :",child.text)