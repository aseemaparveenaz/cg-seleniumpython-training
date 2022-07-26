import xlrd
xl_file = "C:\\Users\OneDrive - Capgemini\Documents\Training\M4\OpenCart\\Unittest_Excel\Login_Invalid.xlsx"

workbook = openpyxl.load_workbook(xl_file)
sheet = workbook.active

rowcount = sheet.max_row
print("Number of rows in excel: ", rowcount-1)

driver = self.driver

for curr_row in range(2, rowcount+1):
driver.get("https://www.opencart.com/index.php?route=account/login")

xl_username = xl.readData(sheet, curr_row, 1)
xl_password = xl.readData(sheet, curr_row, 2)

print("Username: {0} - Password: {1}".format(xl_username, xl_password))

username = driver.find_element_by_id(Locator.login_email)
username.clear()
username.send_keys(xl_username)

password = driver.find_element_by_id(Locator.login_password)
password.clear()
password.send_keys(xl_password)

driver.find_element_by_xpath(Locator.login_button).click()
time.sleep(5)

if (driver.title == "OpenCart - Your Account"):
xl.writeData(sheet, curr_row, 4, "Failed")
else:
xl.writeData(sheet, curr_row, 4, "Passed")
workbook.save(xl_file)

def readData(sheet, row, col):
c1 = sheet.cell(row = row, column = col)
return c1.value

def writeData(sheet, row, col, result_data):
c1 = sheet.cell(row = row, column = col)
c1.value = result_data