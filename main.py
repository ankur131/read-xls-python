

x=3
y=2
z=x+y
print(z)

#f = open('mydata','r')
#print (f.read())

#import openpyxl
#openpyxl.load_workbook("stocks.xlsx")
#sheets=wb.sheetnames
#print(sheets)

import csv
with open('stockscsv.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
     print(row)


import xlrd
loc = ("stocksnew.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
print(sheet.ncols)
print(sheet)

#import openpyxl
#openpyxl.load_workbook("stocks.xlsx")


