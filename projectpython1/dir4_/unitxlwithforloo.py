import xlrd
from selenium import webdriver
loc=(r"C:\Users\ASEEAZ\Desktop\selenuim-python\testsheet1.xls")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
r=1
for r in range(3):

 user=sheet.cell_value(r,0)
 pwd=sheet.cell_value(r,1)
 print(user,"  ",pwd)
 driver=webdriver.Chrome()
 driver.get("https://mail.rediff.com/cgi-bin/login.cgi/")
 driver.find_element_by_xpath("//input[@type='text']").send_keys(user)
 driver.find_element_by_id("password").send_keys(pwd)
 driver.find_element_by_name("proceed").click()
 driver.quit()