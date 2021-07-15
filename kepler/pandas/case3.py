"""
pandas 比较常用的使用函数，
这些函数大致分为6类
统计汇总函数
数据清洗函数
数据筛选
绘图与元素级运算函数
时间序列函数
其他函数
"""



# 数据筛选
"""
注：s指代pandas中的序列对象

函数                       含义                  
s.isin            成员关系判断
s.betweem         区间判断
s.loc             条件判断（可使用在数据框中）
s.iloc            索引判断（可使用在数据框中）
s.compress        条件判断
s.nlargest        搜寻最大的n个元素
s.nsmallest       搜寻最小的n个元素
s.str.findall     子串查询（可使用正则）
"""


# demo
import pandas as pd
import numpy as np

np.random.seed(1234)
x = pd.Series(np.random.randint(10,20,10))

# 筛选出16以上的元素
print(x.loc[x > 16])

print(x.compress(x > 16))

# 筛选出13~16之间的元素
print(x[x.between(13,16)])

# 取出最大的三个元素
print(x.nlargest(3))

y = pd.Series(['ID:1 name:张三 age:24 income:13500',
               'ID:2 name:李四 age:27 income:25000',
               'ID:3 name:王二 age:21 income:8000'])
# 取出年龄，并转换为整数
print(y.str.findall('age:(\d+)').str[0].astype(int))