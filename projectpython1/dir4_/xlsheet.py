import xlrd
import xlwt as xlwt
loc=(r"C:\Users\ASEEAZ\Desktop\selenuim-python\testsheet1.xls")

wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
user=sheet.cell_value(0,0)
pwd=sheet.cell_value(0,1)
print(user)
print(pwd)