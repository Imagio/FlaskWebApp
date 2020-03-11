from app.days import *
from app.subtime import *
from app.subject import *
from app.room import *
from app.group import *


class Lesson(object):
    def __init__(self, weekday, subtime, subject, room, group):
        self.weekday = weekday
        self.subtime = subtime
        self.subject = subject
        self.room = room
        self.group = group


lessons = [
    Lesson(monday, first_subtime, olymp_prog, room453, group10),
    Lesson(monday, second_subtime, programming, room453, group10),
    Lesson(tuesday, first_subtime, programming, room454a, group8),
    Lesson(wednesday, second_subtime, programming, room453, group10),
    Lesson(thursday, first_subtime, programming, room453, group8)
]
