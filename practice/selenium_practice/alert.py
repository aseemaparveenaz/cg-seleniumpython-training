from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/button").click()
ale=driver.switch_to.alert
print(ale.text)
ale.accept()