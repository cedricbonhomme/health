#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import dateutil
import datetime
from manager import Manager
from bootstrap import Base, engine

import models
import scripts

manager = Manager()

@manager.prompt('reinitialize', message='reinitialize the database (yes/no) ?')
@manager.command
def db_initialize(reinitialize='no'):
    "Initialize the database from conf parameters."
    if reinitialize.lower() == 'yes':
        models.db_empty(engine)
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

@manager.arg('base_date', help='Start date', type=str)
@manager.arg('end_date', help='End date', type=str)
@manager.command
def retrieve_weight(base_date, end_date):
    "Retrieve the data about the weight."
    base_date = datetime.datetime.strptime(base_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    assert base_date < end_date, \
                        "base_date should be prior to end_date"
    assert base_date >= end_date - datetime.timedelta(days=31), \
                        "The range should not be longer than 31 days."
    print('Retrieving the weight...')
    scripts.retrieve_bodyweight(base_date, end_date)

@manager.command
def plot_weight():
    "Plot the data about the weight."
    print('Generation of the graph...')
    scripts.plot_weight()


if __name__ == '__main__':
    manager.main()
