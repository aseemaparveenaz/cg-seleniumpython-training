from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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


#enter edit account page
Acc_Page=driver.find_element_by_link_text(locatorr.acc_page)
Acc_Page.click()
print("user entered into account page")

#enter username filed
User_name=driver.find_element_by_name(locatorr.usr)
User_name.clear()
User_name.send_keys("Aseema_parveen")

#enter firstname
Firstname=driver.find_element_by_name(locatorr.fname)
Firstname.clear()
Firstname.send_keys("aseema")

#enter last name
Lastname=driver.find_element_by_name(locatorr.lname)
Lastname.clear()
Lastname.send_keys("AZ")

#enter company name
Company=driver.find_element_by_name(locatorr.comp)
Company.clear()
Company.send_keys("capgemini")

#enter taid
TaxId=driver.find_element_by_name(locatorr.taxid)
TaxId.clear()
TaxId.send_keys("nil")

#enter email
E_mail=driver.find_element_by_name(locatorr.email_)
E_mail.clear()
E_mail.send_keys('aseemaparveenaz@gmail.com')

#select country name from dropdown box
CountryName=Select(driver.find_element(By.ID,locatorr.country))
CountryName.select_by_value("99")

#select radio button
string="yes"
if(string=="no"):
    noti0=driver.find_element_by_css_selector(locatorr.noti_no)
    noti0.click()
else:
    noti1=driver.find_element_by_css_selector(locatorr.noti_yes)
    noti1.click()

#click the button
make_changes="yes"
if(make_changes=="yes"):
    driver.find_element_by_xpath(locatorr.submit_but_acc).click()
    print("account has been edited successfully")
else:
    driver.find_element_by_xpath(locatorr.cancel_but_acc).click()
    print("account has been not edited")
#driver.find_element_by_link_text("CANCEL").click()

time.sleep(5)

#comback to previous page
dashboard=driver.find_element_by_link_text(locatorr.Dashboard).click()
driver.quit()
