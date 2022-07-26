from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/mnjuser/homepage")
# Object of ActionChains
a = ActionChains(driver)
comp = driver.find_element_by_xpath("/html/body/div[1]/div/div/ul[1]/li[3]/a/div")
a.move_to_element(comp).perform()
ques = driver.find_element_by_link_text("Interview Questions")
a.move_to_element(ques).click().perform()
print(driver.title)
time.sleep(10)