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



# 统计汇总函数
"""
注：s指代pandas中的序列对象

函数              含义           
s.min         计算最小值        
s.max         计算最大值
s.sum         求和
s.mean        计算平均数
s.count       计数（统计非缺失元素的个数）
s.size        计数（统计所有元素的个数）
s.median      计算中位数
s.var         计算方差
s.std         计算标准差
s.quantile    计算任意分位数
s.cov         计算协方差
s.corr        计算相关系数
s.skew        计算偏度
s.kurt        计算峰度
s.mode        计算众数
s.describe    描述性统计（一次性返回多个统计结果）
s.groupby     分组
s.aggregete   聚合运算
s.argmin      寻找最小值所在位置
s.argmax      寻找最大值所在位置
s.any         等价于逻辑或
s.all         等价于逻辑与
s.value_counts频次统计 
s.cumsum      运算累计和
s.cumprod     运算累计积
s.pct_change  运算比率（后一个元素与前一个元素的比率）
"""


# demo
import pandas as pd
import numpy as np
x = pd.Series(np.random.normal(2,3,1000))
y = 3*x + 10 + pd.Series(np.random.normal(1,2,1000))

# 计算x与y的相关系数
print(x.corr(y))

# 计算y的偏度
print(y.skew())

# 计算y的统计描述值
print(x.describe())

z = pd.Series(['A','B','C']).sample(n = 1000, replace = True)
# 重新修改z的行索引
z.index = range(1000)
# 按照z分组，统计y的组内平均值
y.groupby(by = z).aggregate(np.mean)

# 统计z中个元素的频次
print(z.value_counts())

a = pd.Series([1,5,10,15,25,30])
# 计算a中各元素的累计百分比
print(a.cumsum() / a.cumsum()[a.size - 1])