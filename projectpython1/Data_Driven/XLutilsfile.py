def readData(loc,sheet,row,col):
    data = sheet.cell_value(row, col)
    return data

def writeData(file,sheetName,rownum,columnno,result):
    wb1=xlwt.Workbook(file)
    sheet = wb1.add_sheet(sheetName)
    sheet.write(rownum,columnno,result)
    wb1.save