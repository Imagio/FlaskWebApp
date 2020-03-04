from app import app
from flask import render_template
from app.days import *
from app.subtime import *


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
    return render_template("schedule.html",
                           day_of_week=get_week_day(),
                           weekdays=weekdays)









