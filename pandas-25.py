import pandas as pd
import numpy as np
##使用默认索引创建Pandas系列
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = pd.Series(nums)
print(s)
##使用自定义索引创建Pandas系列
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s1 = pd.Series(nums1,index=['a','b','c','d','e','f','g','h','i','j'])
print(s1)
nums2 = ['Alan','tinan','jack']
s2 = pd.Series(nums2,index=['1','2','3'])
print(s2)

##从字典创建Pandas系列
dct = {'name':'Alan', 'age':'25'}
s3 = pd.Series(dct)
print(s3)
##创建常量pands系列
s4 = pd.Series(10,index=['a','b','c','d'])
print(s4)
##使用Linspace创建Pandas系列
s5 = pd.Series(np.linspace(5,20,15))
print(s5)
##从列表列表创建数据帧
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

df = pd.DataFrame(data,columns=['name','country','city'])
print(df)

#使用字典创建DataFrame
data1 = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df1 = pd.DataFrame(data1)
print(df1)
#从字典列表创建数据帧
data2 = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df2 = pd.DataFrame(data2)
print(df2)
###head读取前5行
df3 = pd.read_csv('./weight-height.csv')
print(df3)
print("--------head读取前5行--------")
print(df3.head())
##tail读取最后一次记录
print("--------tail读取最后一次记录--------")
print(df3.tail())

print(df3.shape)  ###1000行，3列
print(df3.columns)  ##Index(['Gender', 'Height', 'Weight'], dtype='object')  #获取所有列
print('------使用列键获取特定的列-------')
df4 = df3['Height']
print(df4)
print("--------describe（）info()方法提供数据集的描述性统计值---------")
print(df4.describe())
print('----info()方法提供数据集的描述性统计值----')
print(df.info())
###增加列
print("--------增加列--------")
weight = ['21','36','45']
df2['Weight'] = weight
print(df2)

height = ['171','180','160']
df2['height'] = height
print(df2)
###修改列
df2['height'] = df2['height'].astype(int) ##转换为整数
df2['height'] = df2['height'] * 0.01
print(df2) 
df2['Weight'] = df2['Weight'].astype(int)
df2['Weight'] = df2['Weight'] * 0.45
print(df2)
##修改浮点数
df2['height'] = round(df2['height'],1)
print(df2)
df2['Weight'] = round(df2['Weight'],1)
print(df2)
###增加列
birth_year = ['1997','2002','1999']
curte_year = pd.Series(2024,index=[0,1,2])
df2['birth_year'] = birth_year
df2['curte_year'] = curte_year
print(df2)
##检查数值类型
print(df2.Weight.dtypes) ###float64
###算数新增列
age = df2['curte_year'].astype(int) - df2['birth_year'].astype(int)
df2['age'] = age
print(df2) 

