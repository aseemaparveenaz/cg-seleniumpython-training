from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()
driver.find_element_by_link_text('Login').click()
driver.find_element_by_id('input-email').send_keys('xxx')
driver.find_element_by_id('input-password').send_keys('xxx')
driver.find_element_by_xpath('//div[@class="col-sm-6"]/child::button[1]').submit()
time.sleep(2)
driver.find_element_by_id('input-pin').send_keys('xxx')
driver.find_element_by_xpath('//*[@id="account-security"]/div[2]/div/div[1]/form/div[2]/button').click()
print('Login successful')
change_pwd_page=driver.find_element_by_link_text("Reset your password").click()
oldpwd="xxx"
strpwd=oldpwd[0:5]
intpwd=int(oldpwd[5:])
intpwd=intpwd+1
intpwdstr=str(intpwd)
newpass=strpwd+intpwdstr
curr_pwd=driver.find_element(By.NAME,'current')
curr_pwd.send_keys(oldpwd)
newpassword=driver.find_element(By.NAME,'password')
newpassword.send_keys(newpass)
confirmpassword=driver.find_element(By.NAME,'confirm')
confirmpassword.send_keys(newpass)
#cont_button=driver.find_element_by_xpath("//*[@id='account-password']/div/div/div[1]/form/div/button")
#cont_button.click()
cancel_button=driver.find_element_by_xpath("//*[@id='account-password']/div/div/div[1]/form/div/a")
cancel_button.click()
print("password Changed successfully!")
dashboard=driver.find_element_by_link_text("Dashboard")
driver.quit()
