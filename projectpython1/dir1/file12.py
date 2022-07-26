from selenium import webdriver
webdriver.driver = None
browserName = input("Enter your Browser Name(Chrome/Firefox/Edge): ")
if browserName.lower() == "chrome":
    driver = webdriver.Chrome()
elif browserName.lower() == "firefox":
    driver = webdriver.Firefox()
elif browserName.lower() == "edge":
    driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://www.bing.com")
driver.execute_script("window.open('about:blank', 'thirdtab');")
driver.switch_to.window("thirdtab")
driver.get("https://www.geeksforgeeks.org")