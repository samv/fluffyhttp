import email.utils
import time


class Date:

    @classmethod
    def str2time(cls, date):
        t = int(time.mktime(email.utils.parsedate(date)))
        return t
