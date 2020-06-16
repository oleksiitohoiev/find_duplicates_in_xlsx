import xlrd

loc = 'data.xlsx'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(1, 1)

duplicates = []
shopping_list = []
# loop through all rows
for i in range(sheet.nrows):
  # get value of current column. sheet.cell_value(i, 0)
  # is first field of any row.
  # We can set cell value as (i, 1) if our excel file
  # had multiple   columns in each row.
  value = sheet.cell_value(i, 1)
  # check if value already exists in shopping_list
  # if it does, add to duplicates array
  # if not, add to shopping_list array
  if value in shopping_list:
    duplicates.append(sheet.cell_value(i, 1))
  else:
    shopping_list.append(sheet.cell_value(i, 1))
print(duplicates)