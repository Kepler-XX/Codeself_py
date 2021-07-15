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
注：s指代日期时间型序列，

函数                           含义                  
s.dt.data               抽取出日期值（年-月-日）       
s.dt.time               抽取出时间（时：分：秒）    
s.dt.year               抽取出年
s.dt.month              抽取出月
s.dt.day                抽取出天
s.dt.hour               抽取出小时
s.dt.minute             抽取出分钟
s.dt.second             抽取出秒
s.dt.quarter            抽取出季度
s.dt.weekday            抽取出星期几（返回数值型）
s.dt.weekday_name       抽取出星期几（返回字符型）
s.dt.week               抽取出年中的第几周
s.dt.dayofyear          抽取出年中的第几天
s.dt.daysinmonth        抽取出月对应的最大天数
s.dt.is_month_start     判断日期是否为当月的第一天
s.dt.is_month_end       判断日期是否为当月的最后一天
s.dt.is_quarter_start   判断日期是否为当季度的第一天
s.dt.is_quarter_end     判断日期是否为当季度的最后一天
s.dt.is_year_start      判断日期是否为当年的第一天
s.dt.is_year_end        判断日期是否为当年的最后一天
s.dt.is_leap_year       判断日期是否为闰年
"""