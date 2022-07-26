from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()

banksource = driver.find_element(By.XPATH,"/html/body/section/div/div/main/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
amtsource = driver.find_element(By.XPATH,"/html/body/section/div/div/main/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
bankdest = driver.find_element(By.XPATH,"/html/body/section/div/div/main/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/div/ol/li")
amtdest = driver.find_element(By.XPATH,"/html/body/section/div/div/main/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/div/ol/li")

actions = ActionChains(driver)

actions.drag_and_drop(banksource,bankdest).perform()
actions.drag_and_drop(amtsource,amtdest).perform()
time.sleep(6)
driver.quit()