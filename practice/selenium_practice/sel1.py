""""from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys('selenium python')"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
sel = Select(driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[8]/div/select"))
sel.select_by_index(3)
