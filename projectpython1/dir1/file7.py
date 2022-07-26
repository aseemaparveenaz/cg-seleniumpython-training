
import time
from selenium import webdriver
driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
time.sleep(3)
driver.find_element_by_link_text("org.openqa.selenium.chrome").click()
time.sleep(5)
#driver.switch_to.default_content()
driver.refresh()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("AcceptedW3CCapabilityKeys").click()
time.sleep(3)
