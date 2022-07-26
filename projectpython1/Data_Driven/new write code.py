

import xlrd
import xlwt
from selenium import webdriver
import XL_Utils

loc = ("C:\Geetanjali\Training\Data_Driven\Excel1.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
driver = webdriver.Chrome()
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)
for curr_row in range(1, rowCount):
    username = XL_Utils.readData(loc, 0, curr_row, 0)
    password = XL_Utils.readData(loc, 0, curr_row, 1)
    print(username + " " + password)
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    driver.find_element_by_id("login1").send_keys(username)
    driver.find_element_by_name("passwd").send_keys(password)
    driver.find_element_by_name("proceed").click()
    if driver.title == "Rediffmail":
        XL_Utils.WriteData(loc, "sheet1", curr_row, 3, "testpassed")





