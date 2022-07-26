from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.chrome").click()
driver.switch_to.default_content()
time.sleep(5)
driver.refresh()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("ActiveSession").click()
time.sleep(3)