import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()

actions = ActionChains(driver)

men = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/header/div[2]/nav/div/div[1]/div/a")
actions.move_to_element(men).perform()
time.sleep(3)
t_shirt = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/header/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[2]/a")
actions.context_click(t_shirt).perform()

driver.execute_script("window.open('about:blank' , 'secondtab');")
time.sleep(6)
driver.switch_to.window("secondtab")
driver.get("https://www.myntra.com/men-tshirts")

check_box = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[2]/ul/li[1]/label/div")
actions.click(check_box).perform()
time.sleep(8)
driver.quit()



