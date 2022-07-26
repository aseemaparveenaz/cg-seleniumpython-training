# Open "Google" page in parent window
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title) # 'Google'
# Get parent window
parent_window = driver.current_window_handle
print(parent_window)
# Open "Bing" page in child window
driver.execute_script("window.open('https://bing.com')")
# Get list of all windows currently opened (parent + child)
all_windows = driver.window_handles
print(all_windows)
# Get child window
child_window = [window for window in all_windows if window != parent_window][0]
# Switch to child window
driver.switch_to.window(child_window)
print(driver.title )# 'Bing'
# Close child window
driver.close()
# Switch back to parent window
driver.switch_to.window(parent_window)
print(driver.title) # 'Google'
time.sleep(50)
driver.close()