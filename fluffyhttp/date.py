import email.utils
import time
from datetime import datetime


class Date:

    @classmethod
    def str2time(cls, date):
        t = int(time.mktime(email.utils.parsedate(date)))
        return t

    @classmethod
    def time2str(cls, dt):
        if (isinstance(dt, datetime) is False):
            raise Exception("date is not a datetime object")

        weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
             "Oct", "Nov", "Dec"][dt.month - 1]
        return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month, dt.year, dt.hour, dt.minute, dt.second)
