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



# 其他函数
"""
注：s指代pandas中的序列对象

函数                           含义                  
s.append                序列元素的追加
s.diff                  一阶差分
s.round                 元素的四舍五入
s.sort_values           按值排序
s.sort_index            按索引排序
s.to_dict               转为字典
s.tolist                转为列表
s.unique                元素排重
"""

# demo
import numpy as np
import pandas as pd

np.random.seed(112)
x = pd.Series(np.random.randint(8,18,6))
print(x)
# 对x中的元素做一阶差分
print(x.diff())

# 对x中的元素做降序处理
print(x.sort_values(ascending = False))

y = pd.Series(np.random.randint(8,16,100))
# 将y中的元素做排重处理，并转换为列表对象
y.unique().tolist()