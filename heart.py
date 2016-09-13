#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import Extract

import conf
import models
from bootstrap import Base, session

authd_client = fitbit.Fitbit(conf.CLIENT_KEY, conf.CLIENT_SECRET,
                                access_token=conf.ACCESS_TOKEN,
                                refresh_token=conf.REFRESH_TOKEN)

def get_intraday_time_series(date, detail_level='1min'):
    """
    Return the heart activity.
    """
    heart_activity = authd_client.intraday_time_series(resource= 'activities/heart',
                                                    base_date=date,
                                                    detail_level = detail_level)
    return heart_activity

def insert_database(heart_activity):
    day = dateutil.parser.parse(heart_activity["activities-heart"][0]["dateTime"])
    for elem in heart_activity["activities-heart-intraday"]["dataset"]:
        date = datetime.datetime.combine(day,
                                    dateutil.parser.parse(elem["time"]).time())
        value = float(elem["value"])

        new_bpm = models.Heart(value=value, date=date)
        session.add(new_bpm)
        try:
            session.commit()
        except IntegrityError as e:
            session.rollback()
            pass

def plot(day):

    beats = session.query(models.Heart).filter(
                Extract('day', models.Heart.date) == Extract('day', day)).all()
    dates_x = [elem.date for elem in beats]
    beats_y = [elem.value for elem in beats]

    dates_x_less = [elem for index, elem in enumerate(dates_x) if index%10==0]
    beats_y_less = [elem for index, elem in enumerate(beats_y) if index%10==0]

    fig = plt.figure(figsize=(28, 5), dpi = 400, edgecolor='k')
    ax = fig.add_subplot(111)
    ax.set_xticks(dates_x_less)
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    xfmt = md.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xfmt)

    current_date = heart_activity["activities-heart"][0]["dateTime"]
    plt.suptitle(current_date, fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Heart rate (BPM)', fontsize=16)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=90)

    plt.plot(dates_x_less, beats_y_less, "o-")

    plt.savefig(current_date+'-heart.png', dpi=400, bbox_inches='tight')
    #plt.show()
    plt.clf()
    plt.cla() # clear axis
    del fig


if __name__ == "__main__":

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=2)

    for i in range(3):
        print("Retrieve data about the heart rate...")
        day = today - datetime.timedelta(days=i)
        heart_activity = \
                get_intraday_time_series(day)

        print("Database insertion...")
        insert_database(heart_activity)

        print("Generation of the graph...")
        plot(day)
