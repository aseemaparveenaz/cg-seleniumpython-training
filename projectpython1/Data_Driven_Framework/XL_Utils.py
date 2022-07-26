import openpyxl

def readData(sheet,sheetName,rownum,columnno):
    c1=sheet.cell(row=rownum,column=columnno)
    return c1.value

def WriteData(sheet,filename,rownum,columnno,result):
    c1=sheet.cell(row=rownum,column=columnno)
    c1.value=result