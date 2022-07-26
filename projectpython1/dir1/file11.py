from selenium import webdriver
webdriver.driver=None
browserName=input("enter ur browser name(chrome/firefox/edgeie):")
if browserName.upper()=="CHROME":
    driver=webdriver.Chrome()
elif browserName.upper()=="FIREFOX":
    driver = webdriver.Firefox()
