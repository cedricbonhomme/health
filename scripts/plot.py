#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dateutil
import matplotlib.pyplot as plt
import matplotlib.dates as md
from sqlalchemy.sql import desc
from sqlalchemy.sql.expression import Extract
from sqlalchemy import and_

import models
from bootstrap import session


def plot_heart(day):
    beats = session.query(models.Heart).filter(
            and_(
                Extract('day', models.Heart.date) == Extract('day', day),
                Extract('month', models.Heart.date) == Extract('month', day),
                Extract('year', models.Heart.date) == Extract('year', day),
            )).all()
    if not beats:
        print("No data to plot.")
        return
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

    current_date = day.strftime("%B %d, %Y")
    plt.suptitle(current_date, fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Heart rate (BPM)', fontsize=16)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=90)

    plt.plot(dates_x_less, beats_y_less, "o-")

    plt.savefig(day.strftime("%Y-%m-%d")+'_heart.png', dpi=400,
                bbox_inches='tight')
    #plt.show()
    plt.clf()
    plt.cla() # clear axis
    del fig

def plot_weight():
    weight = session.query(models.Weight).order_by(desc(models.Weight.date)).\
                                            filter().all()
    if not weight:
        print("No data to plot.")
        return
    dates_x = [elem.date for elem in weight]
    weight_y = [elem.value for elem in weight]

    fig = plt.figure(figsize=(40, 5), dpi = 400, edgecolor='k')
    ax = fig.add_subplot(111)
    ax.set_xticks(dates_x)
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    xfmt = md.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(xfmt)

    plt.suptitle("Weight evolution", fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Weight (kg)', fontsize=16)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=90)

    plt.plot(dates_x, weight_y, "o-")

    plt.savefig('weight.png', dpi=400, bbox_inches='tight')
    #plt.show()
    plt.clf()
    plt.cla() # clear axis
    del fig
