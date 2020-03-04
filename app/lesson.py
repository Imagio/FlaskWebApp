from app.days import *
from app.subtime import *
from app.subject import *


class Lesson(object):
    def __init__(self, weekday, subtime, subject):
        self.weekday = weekday
        self.subtime = subtime
        self.subject = subject


lessons = [
    Lesson(monday, first_subtime, olymp_prog),
    Lesson(monday, second_subtime, programming),
    Lesson(tuesday, first_subtime, programming),
    Lesson(wednesday, second_subtime, programming),
    Lesson(thursday, first_subtime, programming)
]
