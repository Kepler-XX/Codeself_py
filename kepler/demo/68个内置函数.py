"""
截至到python3.6.2  python一共提供了68个内置函数，具体如下
abs()           dict()        help()         min()         setattr()
all()           dir()         hex()          next()        slice()
any()           divmod()      id()           object()      sorted()
ascii()         enumerate()   input()        oct()         staticmethod()
bin()           eval()        int()          open()        str()
bool()          exec()        isinstance()   ord()         sum()
bytearray()     ﬁlter()       issubclass()   pow()         super()
bytes()         ﬂoat()        iter()         print()       tuple()
callable()      format()      len()          property()    type()
chr()           frozenset()   list()         range()       vars()
classmethod()   getattr()     locals()       repr()        zip()
compile()       globals()     map()          reversed()    __import__()
complex()       hasattr()     max()          round()
delattr()       hash()        memoryview()   set()

"""

# -----------  和数字相关

# 1.数据类型
bool() # 布尔值
int()  # 整形
float()  # 浮点型
compile()  # 复数
# 2.进制转换
bin()  # 转换为二进制
oct()  # 转换为八进制
hex()  # 转换为十六进制
# 3.数学运算
abs()  # 返回绝对值
divmod()  # 返回商和余数
round()  # 四舍五入
a = 1; b = 2
pow(a,b)  # 求a的b次幂，如果有三个参数，则求完幂后对第三个数取余
sum() # 求和
min() # 求最小值
max() # 求最大值


# --------------- 和数据结构相关

# 1.序列
list() # 将一个可迭代对象转化为列表或者创建一个列表
tuple()  # 将一个可迭代对象转换为元组
reversed() # 将一个序列翻转，返回翻转序列的迭代器
slice() # 列表的切片
str()  # 将数据转化为字符串
bytes()   # 将字符串转化成bytes类型
ord()  # 输入字符找带字符编码的位置
chr()  # 输入位置数字找到对应的字符
ascii()  # 是ascii码中的返回该值，不是返回u
repr()   # 返回一个对象的string形式
dict()   # 创建一个字典
set()    # 创建一个集合
frozenset()  # 创建一个冻结的集合，冻结的集合不能进行添加和删除操作

# 2.相关内置函数
len()  # 返回一个对象中的元素的个数
sorted()  # 将可迭代的对象进行排序操作(lamda)  sorted(Iterable,key=函数（排序规则），reverse=False)
enumerate()  # 获取集合的枚举对象
lst = ['one', 'two', 'three', 'four', 'five']
for index, el in enumerate(lst, 0):
    print(index)
    print(el)

all() # 可迭代对象全部是Ture,结果才是Ture
any() # 可迭代对象有一个是Ture, 结果就是Ture
zip() # 将可迭代对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表，如果各个迭代器的元素个数不一样，则返回列表长度与最短的对象相同
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['醉乡民谣', '驴得水', '放牛班的春天', '美丽人生', '辩护人', '被嫌弃的松子的一生']
lst3 = ['美国', '中国', '法国', '意大利', '韩国', '日本']
print(zip(lst1, lst1, lst3))  #<zip object at 0x00000256CA6C7A88>
for el in zip(lst1, lst2, lst3):
    print(el)


filter() # 过滤（lamda)  filter(function, Iterable)
# case
def func(i):    # 判断奇数
    return i % 2 == 1
lst = [1,2,3,4,5,6,7,8,9]
l1 = filter(func, lst)  #l1是迭代器
print(l1)  #<filter object at 0x000001CE3CA98AC8>
print(list(l1))  #[1, 3, 5, 7, 9]


map() # 根据提供的函数对指定的序列做映射  map(function, iterable)
# case
def f(i):
    return i**2
lst = [1,2,3,4,5,6,7,]
it = map(f, lst)
print(list(it))


# ---------------------其他
locals()  # 返回当前作用域中的名字
globals()  # 返回全局作用域中的名字
range()   # 生成数据
next()   # 迭代器向下执行一次,内部实际使用__next__()方法返回迭代器的下一个项目
iter()   # 获取迭代器，内部实际使用的是__iter__()方法来获取迭代器
eval()   # 执行字符串类型的代码，并返回最终结果
exec()   # 执行字符串类型的代码
compile()   # 将字符串类型的代码编码，代码对象能通过exec语句来执行或者eval()进行求值
"""

s1 = input("请输入a+b:")  #输入:8+9
print(eval(s1))  # 17 可以动态的执行代码. 代码必须有返回值
s2 = "for i in range(5): print(i)"
a = exec(s2) # exec 执行代码不返回任何内容

# 0
# 1
# 2
# 3
# 4
print(a)  #None

# 动态执行代码
exec("""
def func():
    print(" 我是周杰伦")
""" )
func()  #我是周杰伦

code1 = "for i in range(3): print(i)"
com = compile(code1, "", mode="exec")   # compile并不会执行你的代码.只是编译
exec(com)   # 执行编译的结果
# 0
# 1
# 2

code2 = "5+6+7"
com2 = compile(code2, "", mode="eval")
print(eval(com2))  # 18

code3 = "name = input('请输入你的名字:')"  #输入:hello
com3 = compile(code3, "", mode="single")
exec(com3)
"""


print()  # 打印输出
input()   # 获取用户的输入
hash()  # 获取对象的哈希值(int,str,bool,tuple)  hash算法：1.目的是唯一性，2.dict查找效率非常高
                                            # hash表  用空间换的时间比较耗费内存

open() # 用于打开一个文件，创建一个文件句柄
__import__() # 用于动态加载类和函数   __import__(函数名)
help()  # 用于查看函数或者模块用途的详细说明
callable() # 用与检查一个对象是否是可调用的，如果返回Ture,object有可能调用失败，但如果返回Flase,那调用绝对不会成功
dir()  # 查看对象的内置属性，访问的是对象中的__dir__()方法
