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



# 数据清洗函数
"""
注：s指代pandas中的序列对象

函数                       含义                         
s.duplicated           判断序列元素是否重复
s.drop_duplicates      删除重复值
s.hasnans              判断序列是否存在缺失（仅返回True或者False）     
s.isnull               判断序列元素是否为缺失（返回与序列长度一样的bool值）
s.notnull              判断序列元素是否不为缺失（返回与序列长度一样的bool值）
s.dropna               删除缺失值
s.fillna               缺失值补充（使用缺失值的前一个元素补充）
s.ffill                向前填充缺失值（使用缺失值的后一个元素补充）
s.dtypes               检查数据类型
s.astype               类型强制转换
s.to_datatime          转日期时间型
s.factorize            因子化转换
s.sample               抽样
s.where                基于条件判断的值替换
s.replace              按值替换（不可使用正则）
s.str.replace          按值替换（可使用正则， .str不能少）
s.str.split.str        字符分割（.str不能少）
"""

# demo
import pandas as pd
import numpy as np
x = pd.Series([10,13,np.nan,17,28,19,33,np.nan,27])
#检验序列中是否存在缺失值
print(x.hasnans)

# 将缺失值填充为平均值
print(x.fillna(value = x.mean()))

# 前向填充缺失值
print(x.ffill())


income = pd.Series(['12500元','8000元','8500元','15000元','9000元'])
# 将收入转换为整型
print(income.str[:-1].astype(int))

gender = pd.Series(['男','女','女','女','男','女'])
# 性别因子化处理
print(gender.factorize())

house = pd.Series(['大宁金茂府 | 3室2厅 | 158.32平米 | 南 | 精装',
                   '昌里花园 | 2室2厅 | 104.73平米 | 南 | 精装',
                   '纺大小区 | 3室1厅 | 68.38平米 | 南 | 简装'])
# 取出二手房的面积，并转换为浮点型
house.str.split('|').str[2].str.strip().str[:-2].astype(float)
