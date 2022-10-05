import os
import xlrd

sheet_name = "/Users/l3zc/Downloads/校级获奖材料/test/data.xls"
sheet = xlrd.open_workbook(sheet_name)
table = sheet.sheets()[0]   # 加载第一个 sheet
rows_num = table.nrows  # 获取表格的行数
for i in range(1,rows_num):
    row_data = table.row_values(i)
    date = '-' + row_data[5].replace('年','.').replace('月','') # -2022.10
    names = row_data[8].replace('\n','')    # 姓名
    prize_name = row_data[1].replace('\n', '')  # 奖项
    prize_level = row_data[4].replace('\n', '') # 获奖等级
    ext_name = '.' + row_data[13].split(".")[-1]    # 扩展文件名
    rename_dst = str(i) + ' ' + names +' '+ prize_name +' '+ prize_level + date + ext_name
    print(rename_dst)   # 仅调试用
    os.rename(row_data[13], rename_dst)
