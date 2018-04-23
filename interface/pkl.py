# -*- coding:utf-8 -*-
import xlrd
import json
import pickle

xl_file = 'change.xlsx'
wb = xlrd.open_workbook(xl_file)
# 获取第一个sheet
table = wb.sheet_by_index(0)
# 获取总行数
nrows = table.nrows
out_dict = {}
for i in range(table.nrows):
	if i > 0:
		# 获取这一行的所有数据
		row = table.row_values(i)
		ch = row[1]
		out_dict[ch] = int(row[0])

# print(out_dict['祁门县'])
# with open('output_dict.py', 'w') as f:
# 	f.write(json.dumps(out_dict))

# pickle.Pickler('output.pkl').dump(out_dict)

with open('map1.pkl', 'wb') as f:
	pickle.dump(out_dict, f)

# with open('output.pkl', 'rb') as f:
# 	out_dict = pickle.load(f)
#
# print(out_dict['祁门县'])
