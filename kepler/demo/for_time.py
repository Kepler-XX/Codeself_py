import datetime
import random


def str_to_datetime(datetime_str):
    # 字符串转为datetime
    # dd = '2019-03-17 11:00:00'
    dd = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    return dd


def str_to_datetime_for_e(datetime_str_e):
    # 字符串转为datetime
    # datetime_str_e  = '30 July 2021'
    # dd = '2019-03-17 11:00:00'
    dd = datetime.datetime.strptime(datetime_str_e, "%d %B %Y")
    return dd


def get_year():
    # 获取当前年份信息
    year = datetime.datetime.now().year
    return year


def get_month():
    # 获取当前月份信息
    mouth = datetime.datetime.now().month
    return mouth


def get_day():
    # 获取当天日期
    today = datetime.datetime.now().day
    return today


def get_y_m_d():
    # 获取当前日期
    # date = '2020年1月7日'
    date = datetime.date.today()
    return date


def get_h_m_s():
    # 获取当前时分秒
    # tm = '16:13:05'
    tm = datetime.datetime.now().strftime('%X')
    return tm


def random_randint():
    # 随机生成10 - 60 之间的数字
    num = random.randint(10, 59)
    return num