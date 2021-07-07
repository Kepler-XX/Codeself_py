# 短代码
"""
1，二维列表
根据给定的长度和元素个数，以及初始值，返回一个二维列表
"""
import random


def initialize_2d_list(w, h, val=None):
    return [[val for x in range(w)] for y in range(h)]

a = random.randint(1,50)
print(initialize_2d_list(2, 2))
print(initialize_2d_list(3, 2, a))

"""
2,函数切割数组
使用一个函数应用到一个数组的每个元素上，使得这个数组被切割成俩个部分，如果说，函数应用到元素上返回的值为True,
则该元素被切割到第一部分，否则分为第二部分
"""


def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


print(bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b'))


"""
3,最大值下标
返回数组中最大值的下标
"""


def max_element_inde(arr):
    return arr.index(max(arr))


print(max_element_inde([5, 8, 9, 7, 10, 3, 0]))


"""
4，数组对称差
找出两个数组中不同的元素，并合成一个新的数组
"""


def symmetric_difference(a, b):
    _a, _b = set(a), set(b)
    return [item for item in a if item not in _b] +[item for item in b if item not in _a]


print(symmetric_difference([1, 2, 3], [1, 2, 4]))


"""
5,夹数
如果num落在一段数字范围内，则返回num，否则返回离这个范围最近的边界
"""


def clamp_number(num,a,b):
    return max(min(num, max(a,b)), min(a,b))


print(clamp_number(2, 3, 10))


"""
6,大小写转换
将英文单词的首字母大写改为小写
upper_rest参数：设定是否将除首字母外的其他字母大小写转换
"""


def decapitalize(s, upper_rest=False):
    return s[:1].lower() + (s[1:].upper() if upper_rest else s[1:])


print(decapitalize('Foobar'))
print(decapitalize('kepler'))



"""
7,字典相同的键求和
对列表内各个字典里相同键值得对象求和
"""


def sum_by(lst, fn):
    return sum(map(fn, lst))


print(sum_by([{'n': 4}, {'n': 2}, {'n': 8}], lambda v: v['n']))


"""
8,数字转数组
将整形数字拆分到数组中
"""


def digitize(n):
    return list(map(int, str(n)))


print(digitize(123))