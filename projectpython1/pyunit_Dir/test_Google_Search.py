import sys
from selenium.webdriver.common.keys import Keys

sys.path.append(sys.path[0]+"/...")


import unittest
from time import sleep
from pyunit_Dir.WebdriverSetup import WebDriverSetup
from pyunit_Dir.HomePage import Home


class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
        driver=self.driver
        self.driver.get('https://www.google.com/')
        self.driver.set_page_load_timeout(30)


        home=Home(driver)
        home.search_text.send_keys("LambdaTest")
        sleep(5)
        home.search_text.send_keys(Keys.RETURN)
        sleep(10)


if __name__=='main':
    unittest.main()