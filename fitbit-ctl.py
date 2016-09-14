#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dateutil
import datetime
from manager import Manager
from bootstrap import Base

import models
import scripts

manager = Manager()

@manager.command
def db_initialize():
    "Initialize the database from conf parameters."
    Base.metadata.create_all()

@manager.arg('nb_days_from_now', help='The number of days to retrieve from today', type=int)
@manager.command
def retrieve_heart(nb_days_from_now):
    "Retrieve the data about the heart."
    today = datetime.datetime.now()
    for i in range(nb_days_from_now):
        day = today - datetime.timedelta(days=i)
        print('Retrieving the heart rate for {:%B %d, %Y}...'.format(day))
        scripts.retrieve_intraday_time_series(day)

@manager.command
def plot_heart(day):
    "Plot the data about the heart."
    day = dateutil.parser.parse(day)
    print('Generation of the graph...')
    scripts.plot_heart(day)

@manager.arg('nb_days_from_now', help='The number of days to retrieve from today', type=int)
@manager.command
def retrieve_weight(nb_days_from_now):
    "Retrieve the data about the weight."
    today = datetime.datetime.now()
    print('Retrieving the weight...')
    scripts.retrieve_bodyweight(today -
                            datetime.timedelta(days=nb_days_from_now), today)

@manager.command
def plot_weight():
    "Plot the data about the weight."
    print('Generation of the graph...')
    scripts.plot_weight()


if __name__ == '__main__':
    manager.main()
