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
driver.find_element_by_xpath("//*[@id='account-security']/div[2]/div/div[1]/form/div[2]/button").click()
print('Login successful')
#----------
showcase_page=driver.find_element_by_link_text("Submit your store to OpenCart's showcase").click()
print("user entered the showcase page")
add_pro_button=driver.find_element_by_xpath("//*[@id='account-showcase']/div[2]/div/div[1]/div/a[2]")
add_pro_button.click()
print("add project button is clicked")
showcase_name=driver.find_element_by_id("input-name").send_keys("CAR")
showcasetype=Select(driver.find_element(By.ID,"input-category"))
showcasetype.select_by_visible_text('Tech & Gadgets')
time.sleep(2)
launch_date=driver.find_element(By.NAME,"date_launch").send_keys("2021-10-08")
weblink=(driver.find_element(By.ID,"input-link"))
weblink.clear()
weblink.send_keys("https://in.pinterest.com/")
#driver.find_element_by_xpath("//*[@id='account-showcase']/div/div/div[1]/form/fieldset[2]/div/div[1]/div/div").send_keys("C:/Users/ASEEAZ/Desktop/selenuim-python/car.jpg")
time.sleep(20)
submit_button=driver.find_element_by_xpath("//*[@id='account-showcase']/div/div/div[1]/form/div/button").click()
driver.quit()


