import re
import datetime

def yesterday_datetime_start():
    yesterday_start = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + ' ' + "00:00:00"
    return yesterday_start


def yesterday_datetime_end():
    yesterday_end = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + ' ' + "23:59:59"
    return yesterday_end

print(yesterday_datetime_start())
print(yesterday_datetime_end())

