"""
string模块
ascii_letters  用法：string.ascii_letters    获取所有ascii码中字母字符的字符串（包含大写和小写）
ascii_uppercase         获取所有ascii码中的大写英文字母
ascii_lowercase         获取所有ascii码中的小写英文字母
digits                  获取所有的10进制数字字符
octdigits               获取所有的8进制数字字符
hexdigits               获取所有16进制的数字字符
printable               获取所有可以打印的字符
whitespace              获取所有空白字符
punctuation             获取所有的标点符号


ASCII
美国标准信息交换代码。 定制了128个常用字符，主要是英文，数字，标点符号及键盘中其他按键对应的整数值
分别对应如下（特殊符号除外）

A~Z      65~90
a~z      97~122
0~9      48~57


python中与ascii码相关的两个函数
chr()
    将ascii编码转化为字符
    格式：chr(ascii码)
    返回值：字符
ord()
    将字符转化为对应的ascii码
    格式：ord(字符)
    返回值：ascii码
"""

import random
import string

str_ = string.ascii_letters + string.digits  # 大小写字母和数据混装
ran_str = ''.join(random.sample(str_, 15))   # random.sample(str ,number) 随机截取字符串的长度为15

print(f'{str_}')
print(f'{ran_str}')