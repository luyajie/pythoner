#encoding: utf-8
'''自己用的tool
'''

import time
import datetime

def seconds_to_human(seconds, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime(seconds))

def seconds_delta_to_human(seconds):
    return str(datetime.timedelta(seconds=round(seconds)))

def human_to_seconds(string, format='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(string, format))

def today_timestamp():
    return time.mktime(datetime.date.today().timetuple())

def today_human(format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, datetime.date.today().timetuple())
