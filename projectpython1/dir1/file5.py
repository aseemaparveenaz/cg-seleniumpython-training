from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.refresh()
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("Nested Frames").click()
#driver.switch_to_frame("frame-bottom")
driver.switch_to.frame("frame-bottom")
# to get the text inside the frame and print on console
#print(driver.find_element_by_xpath ("//*[text()='BOTTOM']").text)