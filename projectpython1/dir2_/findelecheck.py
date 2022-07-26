from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.refresh()
chk=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(chk))