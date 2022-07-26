from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
s=Select(driver.find_element_by_id("Skills"))
s.select_by_value("Analytics")
