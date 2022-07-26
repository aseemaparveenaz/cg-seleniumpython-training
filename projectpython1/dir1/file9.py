from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
#'Google'
parent_window=driver.current_window_handle
print(parent_window)
#bindg in child window
driver.execute_script("window.open('https://bing.com)")
all_windows=driver.window_handles
#list of all window handles
print(all_windows)
#p+child
child_window=[window for window in all_windows if window!=parent_window][0]
#swith to chid
driver.switch_to.window(child_window)
print(driver.title)
#bing
driver.close()
