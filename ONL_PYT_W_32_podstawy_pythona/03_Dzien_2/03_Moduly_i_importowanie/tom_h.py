import datetime


def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)


print(tomorrow())

# !!! 2-gi sposob na import

# jezeli z pierwszego przykladu z return  usuniemy datatime
# to mozna zmienic opcje importu nie importujac calego datetime
# a zaimportowac tylko paczki

# import datetime import timedelta, date
#
# def tomorrow_2():
#     return date.today() + timedelta(days=1)

# !!! 3-ci sposob na import
# zaimportowac wszsytko z modulu datetime
# from datetime import *


print(tomorrow())
