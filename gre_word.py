import csv

# open .xlsx file
import openpyxl
from openpyxl import Workbook
wb = openpyxl.load_workbook('./GreWordMnemonic.xlsx')
# select the first sheet
sheet = wb.active
#print first sheet
# read all data from excel file
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(list(row))
    # print(list(row))
print(data[1])
flashcard  = dict()
for i in data[:-1]:
    flashcard[i[1]] = i[2]+i[3]

print(flashcard["abate"])