"""from selenium import webdriver"""
"""driver = webdriver.Chrome()
driver.get("https://www.google.com/")

l=[]
l=driver.find_elements_by_tag_name("a")
print(len(l))"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
sel = Select(driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div[8]/div/select"))
sel.select_by_index(3)

"""from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
li=driver.find_elements_by_class_name("ui-corner-all")
for i in li:
    print(i.get_attribute("text"))"""

