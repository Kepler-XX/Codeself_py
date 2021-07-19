import re
kw = '需要匹配的数字为123456，不是111111'


# ^ 元字符，以什么开头
start = re.findall(r'^需要匹配', kw)
print(start)
start1 = re.findall(r'[^\d]', kw)   # 如果写到[]字符集里就是反取, 反取，取出数字之外的字符
print(start1)

#  $ 元字符   以什么结尾
end = re.findall(r'111$', kw)
print(end)

# * 元字符   匹配其前面的一个字符0次或多次
a = re.findall(r'是*', kw)
print(a)

# + 元字符   匹配其前面的一个字符1次或多次
b = re.findall(r'1+', kw)
print(b)

# ？元字符  匹配其前面的一个字符0次或1次
c = re.findall(r'2?', kw)
print(c)

"""
1. {}元字符,范围
{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
{0,}匹配前一个字符0或多次,等同于*元字符
{+,}匹配前一个字符1次或无限次,等同于+元字符
{0,1}匹配前一个字符0次或1次,等同于?元字符

2.[]元字符,字符集
需要字符串里完全符合，匹配规则，就匹配，（规则里的 [] 元字符）对应位置是[]里的任意一个字符就匹配

3.()元字符，分组
也就是分组匹配，()里面的为一个组也可以理解成一个整体
如果()后面跟的是特殊元字符如   (adc)*   那么*控制的前导字符就是()里的整体内容，不再是前导一个字符

4.|元字符，或

|或，或就是前后其中一个符合就匹配

5
\d 匹配任何十进制数，它相当于类[0-9]
\d+如果需要匹配一位或者多位数的数字时用
\D匹配任何非数字字符，它相当于类[^0-9]
\s匹配任何空白字符，它相当于类[\t\n\r\f\v]
\S匹配任何非空白字符，它相当于类[^\t\n\r\f\v]
\w匹配包括下划线在内任何字母数字汉字字符
\W匹配非任何字母数字汉字字符包括下划线在内
"""

# compile 将正则表达式模式编译为正则表达式对象，可使用match(), search()将其用于匹配
prog = re.compile(r'\d+')
skw = prog.search(kw)
mkw = prog.match(kw)
print(prog)
print(skw.group())
print(mkw)

"""
search()函数
search,浏览全部字符串，匹配第一符合规则的字符串，浏览整个字符串去匹配第一个，未匹配成功返回None
search(pattern, string, flags=0)
# pattern： 正则模型
# string ： 要匹配的字符串
# falgs ： 匹配模式
"""
s = re.search(r'\d+', kw)
print(s.group())

"""
match，从头匹配一个符合规则的字符串，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
match(pattern, string, flags=0)
# pattern： 正则模型
# string ： 要匹配的字符串
# falgs ： 匹配模式
"""
m = re.match(r'\d+',kw)
print(m)

"""
findall()函数

findall(pattern, string, flags=0)
# pattern： 正则模型
# string ： 要匹配的字符串
# falgs ： 匹配模式

浏览全部字符串，匹配所有合规则的字符串，匹配到的字符串放到一个列表中，未匹配成功返回空列表

注意：一旦匹配成，再次匹配，是从前一次匹配成功的，后面一位开始的，也可以理解为匹配成功的字符串，不在参与下次匹配"""
lst = re.findall(r'\d+', kw)
print(lst)

# finditer : 匹配字符串中所有的字符，返回的是迭代器
ite = re.finditer(r'\d+', kw)
print([i.group() for i in ite])


"""
sub()函数

替换匹配成功的指定位置字符串

sub(pattern, repl, string, count=0, flags=0)

# pattern： 正则模型
# repl   ： 要替换的字符串
# string ： 要匹配的字符串
# count  ： 指定匹配个数
# flags  ： 匹配模式
"""
rsub = re.sub(r'\d', "s", kw, 2)  # 将匹配到的数字替换成S,替换2个
print(rsub)
rsub = re.sub(r'\d', "s", kw)   # 将匹配到所有的数字替换成S
print(rsub)