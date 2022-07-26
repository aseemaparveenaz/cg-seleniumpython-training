from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/index.htm")
element = driver.find_element_by_link_text("Courses")
print(element.is_enabled())
print(element.is_selected())
print(element.is_displayed())
print(element.parent)