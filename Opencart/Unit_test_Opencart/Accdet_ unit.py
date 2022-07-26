import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Unit_test_Opencart.locator_file import locator

class EditAccount():
    def __init__(self,driver):
        self.driver=driver
        self.ACC_page=driver.find_element_by_link_text(locator.acc_page)
        self.USERname=driver.find_element_by_name(locator.usr)
        self.FIRSTname=driver.find_element_by_name(locator.fname)
        self.LASTname=driver.find_element_by_name(locator.lname)
        self.COMPANYname=driver.find_element_by_name(locator.name)
        self.TAXid=driver.find_element_by_name(locator.taxid)
        self.EMAIL=driver.find_element_by_name(locator.email)
        #self.
        #self.
        s#elf.
   #-----
usr = "username"
fname = "firstname"
lname = "lastname"
comp = "company"
taxid = "tax_id"
email = "email"  # --name
country = 'input-country'  # id
noti_no = "input[value='0']"  # --css selector
noti_yes = "input[value='1']"  # ---css selector
submit_but_acc = "//*[@id='account-edit']/div/div/div[1]/form/div/button"  # xpath
cancel_but_acc = "//*[@id='account-edit']/div/div/div[1]/form/div/a"  # xpath
Dashboard = "Dashboard"  # linktext
acc_page = "Edit your account details"  # link text