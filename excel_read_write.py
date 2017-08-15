# -*- coding:utf-8 -*-
import xlrd

# read excel
data = xlrd.open_workbook('/Users/za/Desktop/ip信用等级/白山云-定位结果-定位详单-20170721-V1.xlsx')
# get the first sheet
table = data.sheets()[0]
# get rows and cols
nrows = table.nrows
ncols = table.ncols
# get the data
row_list = []
for i in range(0,20):
  row_data = table.row_values(i)
  if row_data[4]=='街道':
    row_append = [row_data[0],row_data[5]]
    row_list.append(row_append)
print(len(row_list))
for i in range(0,len(row_list)):
  print(row_list[i])

# write excel
