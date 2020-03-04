from datetime import *

class WeekDay(object):
    def __init__(self, num, name, short_name):
        self.number = num
        self.name = name
        self.short_name = short_name


monday    = WeekDay(1, 'Понедельник', 'ПН')
tuesday   = WeekDay(2, 'Вторник', 'ВТ')
wednesday = WeekDay(3, 'Среда', 'СР')
thursday  = WeekDay(4, 'Четверг', 'ЧТ')
friday    = WeekDay(5, 'Пятница', 'ПТ')


weekdays = [
    monday,
    tuesday,
    wednesday,
    thursday,
    friday
]


def get_week_day():
    now = datetime.now()
    return now.isoweekday()
