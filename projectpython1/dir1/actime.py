from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
var="Please identify yourself"
selvar=driver.find_element_by_id("headerContainer")
print("The identified text is : "+selvar.text)
if(var==selvar.text):
    print("both are same")
else:
    print("not same")
a=driver.find_element_by_id("username").get_attribute("class")
print("The attribute for username is : " +a)