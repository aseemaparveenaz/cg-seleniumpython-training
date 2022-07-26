import openpyxl
import xlrd
import xlwt
import unittest

def readData(sheet, row, col):
    c1 = sheet.cell(row = row, column = col)
    return c1.value

def writeData(sheet, row, col, result_data):
    c1 = sheet.cell(row = row, column = col)
    c1.value = result_data