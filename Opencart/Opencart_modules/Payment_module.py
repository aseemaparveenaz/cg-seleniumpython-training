from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Opencart_modules.locator_ import  locatorr

#login
driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()
driver.find_element_by_link_text(locatorr.login).click()
driver.find_element_by_id(locatorr.email).send_keys('xxx')
driver.find_element_by_id(locatorr.pswd).send_keys('xxx')
driver.find_element_by_xpath(locatorr.loginbtn).submit()
time.sleep(2)
driver.find_element_by_id(locatorr.pin).send_keys('xxx')
driver.find_element_by_xpath(locatorr.subbtn).click()

#switvh to payment page by clicking it
Pay_Page=driver.find_element_by_link_text(locatorr.pay_page).click()
print("user entered the payment page")


#click add card button
AddCard=driver.find_element_by_xpath(locatorr.addcard).click()
time.sleep(5)
#click dropdown
DropDowncre=driver.find_element_by_xpath(locatorr.dropdowncre).click()

time.sleep(20)
print("credential entered manually")

#driver.find_element_by_xpath("//*[@id='credit-card-number']").send_keys(1234567887654321)
#enter the storebutton
StoreButton=driver.find_element_by_id(locatorr.storebutton).click()

print("button is clicked")
