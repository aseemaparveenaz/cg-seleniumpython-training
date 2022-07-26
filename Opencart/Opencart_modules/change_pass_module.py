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

#enter change password page by clicking it
Change_Pwd_Page=driver.find_element_by_link_text(locatorr.change_pwd_page).click()

#password generation
oldpwd="xxx"
strpwd=oldpwd[0:5]
intpwd=int(oldpwd[5:])
intpwd=intpwd+1
intpwdstr=str(intpwd)
newpass=strpwd+intpwdstr

#enter current password
Curr_Pwd=driver.find_element(By.NAME,locatorr.curr_pwd)
Curr_Pwd.send_keys(oldpwd)

#enter neew password
NewPassWord=driver.find_element(By.NAME,locatorr.newpassword)
NewPassWord.send_keys(newpass)

#enter in the cnfirm password field
ConfirmPassWord=driver.find_element(By.NAME,locatorr.confirmpassword)
ConfirmPassWord.send_keys(newpass)

#click submit or cancel button
makechanges="no"
if(makechanges=="yes"):
    Cont_Button=driver.find_element_by_xpath(locatorr.cont_button)
    Cont_Button.click()
    print("password Changed successfully!")
else:
    Cancel_Button=driver.find_element_by_xpath(locatorr.cancel_button)
    Cancel_Button.click()
    print("password not Changed !")

time.sleep(2)


#get back to previous page by clicking dash board
dashboard=driver.find_element_by_link_text("Dashboard")
driver.quit()
