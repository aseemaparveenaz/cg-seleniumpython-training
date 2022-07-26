from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.execute_script("window.open('about:blank','secondtab')")
driver.switch_to.window("secondtab")
driver.get("https://www.geeksforgeeks.org/")