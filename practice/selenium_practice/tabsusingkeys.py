from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/")

ele = driver.find_element_by_xpath('//*[@id="desktop-header-cnt"]/div[2]/nav/div/div[1]/div/a')

action = ActionChains(driver)
action.move_to_element(ele).perform()
sleep(2)
print("parent window ID",driver.current_window_handle)

new_tab = driver.find_element_by_xpath('//*[@id="desktop-header-cnt"]/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[2]/a')
act = ActionChains(driver)
act.key_down(Keys.CONTROL).click(new_tab).key_up(Keys.CONTROL).perform()
sleep(1)

chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
print("child window ID",chwnd)
chk = driver.find_element_by_xpath('//*[@id="mountRoot"]/div/div[1]/main/div[3]/div[1]/section/div/div[2]/ul/li[1]/label/div')
chk.click()
sleep(1)
chk2 = driver.find_element_by_xpath('//*[@id="mountRoot"]/div/div[1]/main/div[3]/div[1]/section/div/div[2]/ul/li[2]/label/div')
chk2.click()
sleep(2)
print("No.of Active tabs:",len(driver.window_handles))
driver.quit()