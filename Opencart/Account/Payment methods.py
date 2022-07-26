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
driver.find_element_by_id('input-password').send_keys('xx')
driver.find_element_by_xpath('//div[@class="col-sm-6"]/child::button[1]').submit()
time.sleep(2)
driver.find_element_by_id('input-pin').send_keys('xx')
driver.find_element_by_xpath("//*[@id='account-security']/div[2]/div/div[1]/form/div[2]/button").click()
print('Login successful')
pay_page=driver.find_element_by_link_text("Modify your payment methods").click()
print("user entered the payment page")
addcard=driver.find_element_by_xpath("//*[@id='paymentDropdown']").click()
dropdowncre=driver.find_element_by_xpath("//*[@id='account-payment']/div/div/div[1]/fieldset/div[2]/span/ul/li[1]/a").click()
print("Enter the credentials")
driver.switch_to.frame(driver.find_element_by_tag_name("fieldset"))

creditcardnum=driver.find_element_by_xpath("//*[@id='credit-card-number']").send_keys(1234567887654321)
#driver.find_element_by_xpath("/html/body/form/input[1]").send_keys(1234567887654321)


cvv=driver.find_element_by_xpath("//*[@id='input-card-cvv']").send_keys(123)
#cvv=driver.find_element_by_id("input-card-cvv").send_keys(123)
storebutton=driver.find_element_by_id("button-continue")
storebutton.click()
print("button is clicked")
