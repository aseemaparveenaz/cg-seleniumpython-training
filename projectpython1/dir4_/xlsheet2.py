import xlrd
import xlwt as xlwt
loc=(r"C:\Users\ASEEAZ\Desktop\selenuim-python\testsheet3.xls")

wb=xlwt.Workbook()
sheet1=wb.add_sheet('sheetnew')
sheet1.write(1,0,'Bangalore')
sheet1.write(3,0,'shastradana')
sheet1.write(5,0,'clemen')
sheet1.write(7,0,'rajpur road')
sheet1.write(9,0,'clock tower')
sheet1.write(0,4,'isbt')
sheet1.write(0,6,'shas')
sheet1.write(0,8,'clemen')
sheet1.write(0,10,'helo')
sheet1.write(0,12,'hi')
wb.save(loc)