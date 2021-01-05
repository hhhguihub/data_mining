from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp, seaborn
from sklearn.preprocessing import MinMaxScaler
import itertools
import xlrd


#将实验1读取成excel的dataframe重新读取出来

excelFile = r'C:\Users\ASUS\Documents\机器学习与数据挖掘\数据文件\\bigTable.xlsx'
bigTable = pd.DataFrame(pd.read_excel(excelFile))

#将体测成绩转换为分数
bigTable.loc[bigTable['Constitution'] == 'bad', 'Constitution'] = 60
bigTable.loc[bigTable['Constitution'] == 'general','Constitution'] = 70
bigTable.loc[bigTable['Constitution'] == 'good','Constitution'] = 80
bigTable.loc[bigTable['Constitution'] == 'excellent','Constitution'] = 90

bigTable['Constitution'] = pd.to_numeric(bigTable['Constitution'],errors='coerce')

print(bigTable)

"""
#1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
mp.style.use('ggplot')  # 设置图表风格 这个是R语言常用的风格

# 散点图

# 绘制散点图查看C1和体能成绩的关系
plt.figure(figsize=(10,10),dpi=100)
plt.scatter(x=bigTable['C1'],y=bigTable['Constitution'],color='b',marker='s')
plt.xlabel('C1')
plt.ylabel('体能成绩')
plt.title('C1_体能成绩关系散点图')

plt.show()

#2. 以5分为间隔，画出课程1的成绩直方图。

#统计C1分数值以及分数值出现的次数
C1_pd = pd.Series(bigTable['C1'])
C1_unique_score = list(C1_pd.value_counts().index)  # 分数的唯一值
Cl_num = list(C1_pd.value_counts())  # 唯一值出现的次数

#绘制直方图
plt.bar(C1_unique_score, Cl_num, width=5)
plt.ylabel('人数')
plt.xlabel('分数')
plt.legend()
plt.show()


#3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。

#将dataframe的列转为矩阵
list_arr=[]
list_arr.append(bigTable['C1'])
list_arr.append(bigTable['C2'])
list_arr.append(bigTable['C3'])
list_arr.append(bigTable['C4'])
list_arr.append(bigTable['C5'])
list_arr.append(bigTable['C6'])
list_arr.append(bigTable['C7'])
list_arr.append(bigTable['C8'])
list_arr.append(bigTable['C9'])
list_arr.append(bigTable['Constitution'])

arr = np.array(list_arr)
print(arr)
print()

#将数据集进行归一化处理
scaler = MinMaxScaler( )
scaler.fit(arr)
scaler.data_max_
my_matrix_normorlize=scaler.transform(arr)
print(my_matrix_normorlize)

"""

#4. 计算出107x107的相关矩阵，并可视化出混淆矩阵。

#取出要计算相关系数的列
list = []
list.append(bigTable['Height'])
list.append(bigTable['C1'])
list.append(bigTable['C2'])
list.append(bigTable['C3'])
list.append(bigTable['C4'])
list.append(bigTable['C5'])
list.append(bigTable['C6'])
list.append(bigTable['C7'])
list.append(bigTable['C8'])
list.append(bigTable['C9'])
list.append(bigTable['Constitution'])

list_fin=[[r[col] for r in list] for col in range(len(list[0]))] #行列转换

table = pd.DataFrame(list_fin, columns=['Height', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'Constitution'])
print(table)

#求相关矩阵
table_corr = table.corr()

# 可视化
seaborn.heatmap(table_corr, center=0, annot=True, cmap='YlGnBu')
mp.show()

print(table_corr)