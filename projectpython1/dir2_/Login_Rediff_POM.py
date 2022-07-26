import unittest
from selenium import webdriver
from seleniumpagefactory import PageFactory

class LoginPage1(PageFactory):
    def __init__(self,driver):
        self.driver = driver
    locators = {
        "edtUserName": ('ID', 'login1'),
        "edtPassword": ('NAME', 'passwd'),
        "btnSignIn": ('XPATH', '//input[@name="proceed"]')

    }
    def login(self):
        self.edtUserName.set_text("username")
        self.edtPassword.set_text("xxxxxx")
        self.btnSignIn.click_button()
class LoginTest(unittest.TestCase):

    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        pgLogin = LoginPage1(driver)
        pgLogin.login()