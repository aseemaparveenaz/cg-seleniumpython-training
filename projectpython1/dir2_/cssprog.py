from selenium import webdriver
driver=webdriver.Chrome()
keyword="geeksforgeeks"
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
element=driver.find_element_by_css_selector("input[type='text']")
element.send_keys("aseema")
print(element)
