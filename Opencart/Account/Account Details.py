from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()

#-------login
driver.find_element_by_link_text('Login').click()
driver.find_element_by_id('input-email').send_keys('xxxx')
driver.find_element_by_id('input-password').send_keys('xxx')
driver.find_element_by_xpath('//div[@class="col-sm-6"]/child::button[1]').submit()
time.sleep(2)
driver.find_element_by_id('input-pin').send_keys('xx')
driver.find_element_by_xpath('//*[@id="account-security"]/div[2]/div/div[1]/form/div[2]/button').click()
print('Login successful')



acc_page=driver.find_element_by_link_text("Edit your account details")
acc_page.click()
print("user entered into account page")
usr=driver.find_element_by_name("username")
usr.clear()
usr.send_keys("Aseema_parveen")
fname=driver.find_element_by_name("firstname")
fname.clear()
fname.send_keys("aseema")
lname=driver.find_element_by_name("lastname")
lname.clear()
lname.send_keys("AZ")
comp=driver.find_element_.by_name("company")
comp.clear()
comp.send_keys("capgemini")
taxid=driver.find_element_by_name("tax_id")
taxid.clear()
taxid.send_keys("nil")
email=driver.find_element_by_name("email")
email.clear()
email.send_keys('aseemaparveenaz@gmail.com')
country=Select(driver.find_element(By.ID,'input-country'))
country.select_by_value("98")
noti=driver.find_element_by_css_selector("input[value='0']")
noti.click()
#driver.find_element_by_xpath("//*[@id='account-edit']/div/div/div[1]/form/div/button").click()
driver.find_element_by_xpath("//*[@id='account-edit']/div/div/div[1]/form/div/a").click()
#driver.find_element_by_link_text("CANCEL").click()
print("account has beed edited successfully")
time.sleep(5)
#dashboard=driver.find_element_by_link_text("Dashboard").click()
driver.quit()