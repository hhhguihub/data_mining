import pandas as pd
import xlrd

#将上一步读取成excel的dataframe重新读取出来

excelFile = r'C:\Users\ASUS\Documents\机器学习与数据挖掘\数据文件\\bigTable.xlsx'
bigTable = pd.DataFrame(pd.read_excel(excelFile))
print(bigTable)


#第四步： 数据处理

#1. 学生中家乡在Beijing的所有课程的平均成绩。

# 要被group的列名
Beijing = bigTable.loc[bigTable['City']=='Beijing']

print("北京学生C1均值为： ",Beijing['C1'].mean() )   #计算每列均值
print("北京学生C2均值为： ",Beijing['C2'].mean() )   #计算每列均值
print("北京学生C3均值为： ",Beijing['C3'].mean() )   #计算每列均值
print("北京学生C4均值为： ",Beijing['C4'].mean() )   #计算每列均值
print("北京学生C5均值为： ",Beijing['C5'].mean() )   #计算每列均值
print("北京学生C6均值为： ",Beijing['C6'].mean() )   #计算每列均值
print("北京学生C7均值为： ",Beijing['C7'].mean() )   #计算每列均值
print("北京学生C8均值为： ",Beijing['C8'].mean() )   #计算每列均值
print("北京学生C9均值为： ",Beijing['C9'].mean() )   #计算每列均值

#2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。

Guangzhou = bigTable.loc[bigTable['City']=='Guangzhou']
GB_sum = len(Guangzhou[(Guangzhou['C1'] >80 )&(Guangzhou['C9'] > 9)&(Guangzhou['Gender'] == 'boy')])
print("学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量为：",GB_sum)
print()


#3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
##  体能测试成绩（string：差/一般/良好/优秀）,假设差为60分，一般为70分，良好为80分，优秀为90分

#北京的平均体能测试成绩
B_bad = (Beijing["Constitution"]=="bad").sum()
B_general = (Beijing["Constitution"]=="general").sum()
B_good = (Beijing["Constitution"]=="good").sum()
B_excellent = (Beijing["Constitution"]=="excellent").sum()

B_constitution =(B_bad*60 + B_general*70 + B_good*80 +B_excellent*90)/(B_bad + B_general + B_good +B_excellent)

#上海的平均体能测试成绩
Shanghai = bigTable.loc[bigTable['City']=='Shanghai']
S_bad = (Shanghai["Constitution"]=="bad").sum()
S_general = (Shanghai["Constitution"]=="general").sum()
S_good = (Shanghai["Constitution"]=="good").sum()
S_excellent = (Shanghai["Constitution"]=="excellent").sum()

S_constitution =(S_bad*60 + S_general*70 + S_good*80 +S_excellent*90)/(S_bad + S_general + S_good +S_excellent)

#比较两地成绩并输出
if(B_constitution>S_constitution):
    print("北京地区更强。")
elif(S_constitution>B_constitution):
    print("上海地区更强。")
else:
    print("两地区一样强。")
print()

#4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

bigTable.loc[bigTable['Constitution'] == 'bad', 'Constitution'] = 60
bigTable.loc[bigTable['Constitution'] == 'general','Constitution'] = 70
bigTable.loc[bigTable['Constitution'] == 'good','Constitution'] = 80
bigTable.loc[bigTable['Constitution'] == 'excellent','Constitution'] = 90

bigTable['Constitution'] = pd.to_numeric(bigTable['Constitution'],errors='coerce')

print("体测成绩”与“C1”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C1'])) #计算“体测成绩”与“C1”的相关系数
print("体测成绩”与“C2”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C2'])) #计算“体测成绩”与“C2”的相关系数
print("体测成绩”与“C3”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C3'])) #计算“体测成绩”与“C3”的相关系数
print("体测成绩”与“C4”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C4'])) #计算“体测成绩”与“C4”的相关系数
print("体测成绩”与“C5”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C5'])) #计算“体测成绩”与“C5”的相关系数
print("体测成绩”与“C6”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C6'])) #计算“体测成绩”与“C6”的相关系数
print("体测成绩”与“C7”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C7'])) #计算“体测成绩”与“C7”的相关系数
print("体测成绩”与“C8”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C8'])) #计算“体测成绩”与“C8”的相关系数
print("体测成绩”与“C9”的相关系数为： ",bigTable[u'Constitution'].corr(bigTable[u'C9'])) #计算“体测成绩”与“C9”的相关系数