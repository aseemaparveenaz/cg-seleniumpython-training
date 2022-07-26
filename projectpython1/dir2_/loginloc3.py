import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dir2_.Locators3 import Locatorr

class LoginPage1():
    def __init__(self, driver):
        self.driver = driver
        self.editUserName = driver.find_element(By.ID, Locatorr.username)
        self.editPassword = driver.find_element(By.NAME, Locatorr.password)
        self.btnSignIn = driver.find_element(By.XPATH, Locatorr.button)

    def login(self):
        self.editUserName.send_keys("uname")
        self.editPassword.send_keys("xxx")
        self.btnSignIn.click()

class LoginTest(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

        pglogin = LoginPage1(driver)
        pglogin.login()