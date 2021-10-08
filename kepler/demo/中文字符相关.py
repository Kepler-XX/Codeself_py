#  检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


# 检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


# 检验所有字符是否都是数字或者字母
def is_all_number_or_letter(strs):
    strs.isalnum()
    pass


# 检验所有字符是否都是字母
def is_all_letter(strs):
    strs.isalpha()
    pass


# 检验所有字符是否都是数字
def is_all_number(strs):
    strs.isdigit()
    pass


# 检验所有字符是否都是小写
def is_all_lower(strs):
    strs.islower()
    pass


# 检验所有字符是否都是大写
def is_all_upper(strs):
    strs.isupper()
    pass


# 检验所有字符首字母是否为大写
def is_first_upper(strs):
    strs.istitle()
    pass


# 检验所有字符是否都是空白符
def is_all_space(strs):
    strs.isspace()
    pass


if __name__ == '__main__':
    while 1:
        kw = input("请输入字符")
        print(is_all_chinese(kw))