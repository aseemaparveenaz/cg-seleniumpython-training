from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.refresh()
driver.find_element_by_link_text("Click Here").click()
#focus#idcomes
print(driver.current_window_handle)
chwnd=driver.window_handles[1]
print(chwnd)
driver.switch_to.window(chwnd)
print(driver.find_element_by_tag_name("h3").text)