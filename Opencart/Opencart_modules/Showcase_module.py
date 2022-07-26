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

#enter into showcase page by clicking it
Showcase_Page=driver.find_element_by_link_text(locatorr.showcase_page).click()
print("user entered the showcase page")

#click add project button
Add_Pro_Button=driver.find_element_by_xpath(locatorr.add_pro_button)
Add_Pro_Button.click()
print("add project button is clicked")

#enter shocwcase name
Showcase_Name=driver.find_element_by_id(locatorr.showcase_name).send_keys("CAR")

#enter showcase type from drop down
ShowcaseType=Select(driver.find_element(By.ID,locatorr.showcasetype))
ShowcaseType.select_by_visible_text('Tech & Gadgets')
time.sleep(2)

#enter the launch date
Launch_Date=driver.find_element(By.NAME,locatorr.launch_date).send_keys("2021-10-08")

#enter weblink
WebLink=(driver.find_element(By.ID,locatorr.weblink))
WebLink.clear()
WebLink.send_keys("https://in.pinterest.com/")

print("image uploaded manually")
#driver.find_element_by_xpath("//*[@id='account-showcase']/div/div/div[1]/form/fieldset[2]/div/div[1]/div/div").send_keys("C:/Users/ASEEAZ/Desktop/selenuim-python/car.jpg")
time.sleep(20)

#click button submit or cancel
change="no"
if(change=="yes"):
    submit_button=driver.find_element_by_xpath(locatorr.submit_button).click()
else:
    CANCEL_button=driver.find_element_by_xpath(locatorr.canc_show).click()


driver.quit()