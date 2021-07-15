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



# 绘图与元素级运算函数
"""
注：s指代pandas中的序列对象

函数                       含义                  
s.hist              绘制直方图
s.plot              可基于kind参数绘制更多图形（饼图，折线图，箱线图）
s.map               元素映射
s.apply             基于自定义函数的元素级操作
"""


# demo

import pandas as pd
import numpy as np
np.random.seed(123)
import matplotlib.pyplot as plt
x = pd.Series(np.random.normal(10,3,1000))
# 绘制x直方图
x.hist()
# 显示图形
plt.show()

# 绘制x的箱线图
x.plot(kind='box')
plt.show()

installs = pd.Series(['1280万','6.7亿','2488万','1892万','9877','9877万','1.2亿'])
# 将安装量统一更改为“万”的单位
def transform(x):
    if x.find('亿') != -1:
        res = float(x[:-1])*10000
    elif x.find('万') != -1:
        res = float(x[:-1])
    else:
        res = float(x)/10000
    return res
installs.apply(transform)