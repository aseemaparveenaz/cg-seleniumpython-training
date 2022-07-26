from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.rediff.com/")
inputElement = driver.find_element_by_xpath("//*[contains(@placeholder,'Search news')]")
inputElement.send_keys("tcs")
inputElement.submit()