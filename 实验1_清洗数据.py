import pandas as pd
import  xlrd

#第一步： 把excel的数据读入列表中

file_path = r'C:\Users\ASUS\Documents\机器学习与数据挖掘\数据文件\\data1.xlsx'
datas_1 = []  # 存储处理后的数据
data = xlrd.open_workbook(file_path)  # open the excel file
table = data.sheets()[0]  # open the first sheet
row_n = table.nrows
for i in range(1, row_n):
    col = table.row_values(i)  # 获取每一行数据new.py
    datas_1.append(col)

#将类型换成浮点型，便于合并
table1 = pd.DataFrame(datas_1, columns=['ID', 'Name', 'City', 'Gender', 'Height', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'Constitution'])
table1['ID'] = pd.to_numeric(table1['ID'],errors='coerce')
table1['C1'] = pd.to_numeric(table1['C1'],errors='coerce')
table1['C2'] = pd.to_numeric(table1['C2'],errors='coerce')
table1['C3'] = pd.to_numeric(table1['C3'],errors='coerce')
table1['C4'] = pd.to_numeric(table1['C4'],errors='coerce')
table1['C5'] = pd.to_numeric(table1['C5'],errors='coerce')
table1['C6'] = pd.to_numeric(table1['C6'],errors='coerce')
table1['C7'] = pd.to_numeric(table1['C7'],errors='coerce')
table1['C8'] = pd.to_numeric(table1['C8'],errors='coerce')
table1['C9'] = pd.to_numeric(table1['C9'],errors='coerce')

print(table1)


#第二步： 把txt的数据读入列表中

filepath = r'C:\Users\ASUS\Documents\机器学习与数据挖掘\数据文件\\data2.txt'
fp = open(filepath, "r")
datas_2 = []  # 存储处理后的数据
lines = fp.readlines()  # 读取整个文件数据

for line in lines[1:]:
    row = line.strip('\n').replace("female","girl")  # 去除两头的换行符，按空格分割
    row=row.replace("male","boy").split(',')
    row[0]=float(eval(row[0])-202000)
    row[4]=str(int((eval(row[4])*100)))
    datas_2.append(row)

table2 = pd.DataFrame(datas_2, columns=['ID', 'Name', 'City', 'Gender', 'Height', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'Constitution'])

#将类型换成浮点型，便于合并
table2['ID'] = pd.to_numeric(table2['ID'],errors='coerce')
table2['C1'] = pd.to_numeric(table2['C1'],errors='coerce')
table2['C2'] = pd.to_numeric(table2['C2'],errors='coerce')
table2['C3'] = pd.to_numeric(table2['C3'],errors='coerce')
table2['C4'] = pd.to_numeric(table2['C4'],errors='coerce')
table2['C5'] = pd.to_numeric(table2['C5'],errors='coerce')
table2['C6'] = pd.to_numeric(table2['C6'],errors='coerce')
table2['C7'] = pd.to_numeric(table2['C7'],errors='coerce')
table2['C8'] = pd.to_numeric(table2['C8'],errors='coerce')
table2['C9'] = pd.to_numeric(table2['C9'],errors='coerce')

print(table2)

fp.close()


#第三步： 合并两个表格的数据

bigTable = pd.merge(table1, table2, on=['ID', 'Name', 'City', 'Gender', 'Height', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'Constitution'], how='outer')
bigTable = bigTable.drop_duplicates(keep='first')
print(bigTable)


#第四步：将bigTable读入excel

bigTable.to_excel(r'C:\Users\ASUS\Documents\机器学习与数据挖掘\数据文件\\bigTable.xlsx', index =True, header=True)