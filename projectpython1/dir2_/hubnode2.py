from selenium import webdriver

driver = webdriver.Remote(
    command_executor="http://192.168.0.185:9005/wd/hub",
    desired_capabilities={"browserName": "chrome",
                          'javascriptEnabled': True,
                          'platform': 'WINDOWS'}
    )
driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys("hi")
driver.find_element_by_id("pass").send_keys("hello")
driver.find_element_by_id("login").click()