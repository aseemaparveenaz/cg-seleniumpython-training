from selenium import webdriver
import  xlrd
from Data_Driven import XLutilsfile
driver = webdriver.Chrome()
loc=(r"C:\Users\ASEEAZ\Desktop\selenuim-python\testsheet1.xls")
work_book=xlrd.open_workbook(loc)
sheet=work_book.sheet_by_index(0)
rowCount = sheet.nrows
columnCount = sheet.ncols
print(rowCount)
print(columnCount)
for curr_row in range(0, rowCount):
    user = XLutilsfile.readData(loc,sheet,curr_row, 0)
    password = XLutilsfile.readData(loc,sheet,curr_row, 1)

    print(user + " " + password)
    driver.get("https://mail.rediff.com/")
    driver.find_element_by_link_text("Sign in").click()
    username=driver.find_element_by_id("login1").send_keys(user)
    password=driver.find_element_by_name("passwd").send_keys(password)
    signIn=driver.find_element_by_xpath("//input[@name='proceed']").click()
    username.send_keys(user)
    password.send_keys(password)
    signIn.click()
