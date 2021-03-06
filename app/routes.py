from app import app
from flask import render_template
from app.days import *
from app.subtime import *
from app.subject import *
from app.lesson import *


class User(object):
    def __init__(self, name):
        self.user_name = name


@app.route('/')
@app.route('/index/<name>')
def index(name="unknown"):
    return render_template("index.html",
                           title="Заголовок",
                           user=User(name))


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/schedule')
def schedule():
    schedule_data=[]

    class ScheduleRow(object):
        def __init__(self, subtime):
            self.subtime=subtime
            self.lessons=[None for day in weekdays]

    for subtime in subtimes:
        schedule_data.append(ScheduleRow(subtime))
    
    for lesson in lessons:
        row = lesson.subtime.number - 1
        column = lesson.weekday.number - 1
        schedule_data[row].lessons[column] = lesson

    return render_template("schedule.html",
                           day_of_week=get_week_day(),
                           weekdays=weekdays,
                           data=schedule_data)









