import xlrd
import xlwt
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
loc = (r"C:\Users\ASEEAZ\Desktop\selenuim-python\testsheet1.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
user = sheet.cell_value(1,0)
pwd = sheet.cell_value(1,1)
print(user)
print(pwd)
class LoginPage1():
    def __init__(self, driver):
        self.driver = driver
        self.username = "login1"
        self.password = "passwd"
        self.button = "//input[@name = 'proceed']"
        self.editUserName = driver.find_element(By.ID, self.username )
        self.editPassword = driver.find_element(By.NAME,  self.password)
        self.btnSignIn = driver.find_element(By.XPATH,  self.button)

    def login(self):
        self.editUserName.send_keys(user)
        self.editPassword.send_keys(pwd)
        self.btnSignIn.click()

class LoginTest(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

        pglogin = LoginPage1(driver)
        pglogin.login()