from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.softwaretestingmaterial.com/")

#to add cookies
driver.add_cookie({'name': 'f', 'value': 'v'})

#to get cookie with name
print(driver.get_cookie('f'))

#to get all cookie
print(driver.get_cookies())

#to delete a cookie with name
driver.delete_cookie('f')

#todelete all cookie
driver.delete_all_cookies()

driver.close()