import sys
sys.path.append(sys.path[0]+"/...")
import unittest
from time import sleep
from pyunit_Dir.WebdriverSetup import WebDriverSetup
from pyunit_Dir.HomePage import Home
from selenium import webdriver

class Google_Homepage(WebDriverSetup):

    def test_Home_Page(self):
        driver=self.driver
        self.driver.get("http://www.google.com/")
        self.driver.set_page_load_timeout(30)

        web_page_title="Google"

        try:
            if driver.title==web_page_title:
                print("Webpage loaded succcessfully !")
                self.assertEqual(driver.title,web_page_title)
        except Exception as error:
            print(error+"Webpage Failed to Load")

        home_page= Home(driver)


if __name__=='main':
    unittest.main()