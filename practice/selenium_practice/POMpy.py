import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_practice.gitlocator import GitLocator

class GitLoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.editUserName = driver.find_element(By.ID, GitLocator.username)
        self.editPassword = driver.find_element(By.NAME, GitLocator.password)
        self.btnSignIn = driver.find_element(By.XPATH, GitLocator.button)
    def login(self):
        self.editUserName.send_keys("uname")
        self.editPassword.send_keys("xxxx")
        self.btnSignIn.click()

class Homepage():
    def __init__(self,driver):
        self.driver=driver
        self.Readbutton=driver.find_element(By.XPATH,GitLocator.readguidebutton)
    def homepage(self):
        self.Readbutton.click()
        time.sleep(5)

class LoginTest(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://github.com/login")
        pglogin = GitLoginPage(driver)
        pglogin.login()
        Homepageobj=Homepage(driver)
        Homepageobj.homepage()

