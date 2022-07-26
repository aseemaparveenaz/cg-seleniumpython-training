from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_name("proceed").click()
wait=WebDriverWait(driver,15)
ale=driver.switch_to.alert
print(ale.text)
ale.accept()