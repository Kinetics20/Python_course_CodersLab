#!/usr/bin/python3
import datetime
from datetime import timedelta, date


def tomorrow():
    # return date.today() + timedelta(days=1)
    return datetime.date.today() + datetime.timedelta(days=1)


print(tomorrow())
