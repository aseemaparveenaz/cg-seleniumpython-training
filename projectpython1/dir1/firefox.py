from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.rediff.com/")
#driver.find_element_by_partial_link_text("Sign in").click()
driver.find_element_by_partial_link_text("Sign").click()
driver.find_element_by_xpath("//*[@type='text']").send_keys("")
driver.find_element_by_id("password").send_keys("")
driver.find_element_by_name("proceed").click()
driver.find_element_by_class_name("rd_logout").click()