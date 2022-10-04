import os
import xlrd

sheet_name = "/Users/l3zc/Downloads/校级获奖材料/test/data.xls"
sheet = xlrd.open_workbook(sheet_name)
table = sheet.sheets()[0]   # 加载第一个 sheet
rows_num = table.nrows  # 获取表格的行数
for i in range(1,rows_num):
    row_data = table.row_values(i)
    date = '-' + row_data[5].replace('年','.').replace('月','') # -2022.10
    rename_dst = str(i) + ' ' + row_data[8].replace('\n', '') +' '+ row_data[1].replace('\n', '') + ' '+ row_data[4].replace('\n', '') + date + '.' + row_data[13].split(".")[-1]
    print(rename_dst)   # 仅调试用
    os.rename(row_data[13], rename_dst)
    


'''
names_src = os.listdir(path)
os.rename(names_src[0],"电气工程" + "." + names_src[0].split(".")[1])
'''
