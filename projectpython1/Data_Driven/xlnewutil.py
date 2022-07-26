import unittest
import xlrd
import xlwt


def readData(file, sheetName, rownum, columnno):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(sheetName)
    return sheet.cell_value(rowx=rownum, colx=columnno)


def WriteData(file, sheetName, rownum, columnno, result):
    wb1 = xlwt.Workbook(file)
    sheet = wb1.add_sheet(sheetName)
    sheet.write(rownum, columnno, result)
    wb1.save