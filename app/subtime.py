class Subtime(object):
    def __init__(self, num, start_time, end_time):
        self.number = num
        self.start_time = start_time
        self.end_time = end_time


first_subtime = Subtime(1, "15:30", "16:50")
second_subtime = Subtime(2, "17:00", "18:20")


subtimes=[
    first_subtime,
    second_subtime
]
