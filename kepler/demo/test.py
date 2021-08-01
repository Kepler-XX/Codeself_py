# 常用的函数

# 1.把字符串型的list转化为list
# 使用ast模块中的literal_eval函数来实现，把字符串形式的list转换为Python的基础类型list

from ast import literal_eval

str_list = "[1838, 13735, 8285, 35386]"
ls = literal_eval(str_list)
print(f'type:{type(ls)}--ls:{ls}')

# 2.  filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#  该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
#  最后将返回 True 的元素放到新列表中。

# Python3.x 返回的结果是迭代器对象，可以使用list()函数把迭代器对转转换为列表对象，例如
ret = filter(lambda x: x % 2 == 0, range(10))
print(list(ret))


# 当对List、Dict进行排序时，Python提供了两个方法：
        # 用List的成员函数sort进行排序，在本地进行排序，不返回副本
        # 用built-in函数sorted进行排序（从2.4开始），返回副本，原始输入不变
# 在本质上，list的排序和内建函数sorted的排序是差不多的，连参数都是一样的，
# 主要区别在于，list.sort()是对已经存在的列表进行操作，进而可以改变列表；而内建函数sorted返回的是一个新的list，
# 而不是在原来的基础上进行的操作。返回值是一个经过排序的可迭代类型，与iterable是一样的。

