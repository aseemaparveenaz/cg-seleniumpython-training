import unittest
from selenium import webdriver
import time
import openpyxl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from roughaccdir import fynctnrdwt
from roughaccdir.Locattor import Locatorr
class Edit_Acc_page(unittest.TestCase):
    @classmethod
    def setUpClass(class_name):
      class_name.driver = webdriver.Chrome()
      class_name.driver.maximize_window()

    def setUp(self):
        print("test case executing...")

    def test0_Login_valid(self):
        xl_file = r"C:\Users\ASEEAZ\Desktop\selenuim-python\opencart_project\opencartxlsheet.xlsx"
        workbook = openpyxl.load_workbook(xl_file)
        sheet = workbook.active
        rowcount = sheet.max_row
        print("Number of rows in excel: ", rowcount - 1)
        for curr_row in range(2, rowcount + 1):
            self.driver.get("https://www.opencart.com/index.php?route=account/login")
            xl_username = fynctnrdwt.readData(sheet, curr_row, 1)
            xl_password = fynctnrdwt.readData(sheet, curr_row, 2)
            xl_pin      = fynctnrdwt.readData(sheet,curr_row,3)
            print("Username: {0} - Password: {1}".format(xl_username, xl_password))
            username = self.driver.find_element_by_id(Locatorr.email)
            username.clear()
            username.send_keys(xl_username)
            password = self.driver.find_element_by_id(Locatorr.pswd)
            password.clear()
            password.send_keys(xl_password)
            self.driver.find_element_by_xpath(Locatorr.loginbtn).click()
            time.sleep(5)
            try:
                if self.driver.find_element_by_id(Locatorr.pin).is_displayed():
                    pinn=self.driver.find_element_by_id(Locatorr.pin)
                    pinn.clear()
                    pinn.send_keys(xl_pin)
                    self.driver.find_element_by_xpath(Locatorr.subbtn).submit()
                    time.sleep(6)
            except NoSuchElementException:
                fynctnrdwt.writeData(sheet, curr_row, 4, "failed")
        if (self.driver.title == "OpenCart - Your Account"):
            fynctnrdwt.writeData(sheet, curr_row, 4, "passed")
            print('Login successful')
        else:
            print("login failed")
        workbook.save(xl_file)


    def tearDown(self):
        print("testcase executed")

    @classmethod
    def tearDownClass(class_name):
        class_name.driver.quit()
        print("compltd")
