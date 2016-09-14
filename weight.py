#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import datetime
from sqlalchemy.exc import IntegrityError

import conf
import models
from bootstrap import Base, session

client_kwargs = {
        'client_id': conf.CLIENT_KEY,
        'client_secret': conf.CLIENT_SECRET,
        'callback_uri': 'https://dev.fitbit.com',
        'scope': ['sleep+settings+nutrition+activity+social+heartrate+profile+weight+location']
}

fb_client = fitbit.Fitbit(conf.CLIENT_KEY, conf.CLIENT_SECRET,
                        access_token=conf.ACCESS_TOKEN, refresh_token=conf.REFRESH_TOKEN)


def get_bodyweight(base_date, end_date=None):
    """
    Return data about the body weight.
    """
    weight = fb_client.get_bodyweight(base_date=base_date, end_date=end_date)
    return weight

def insert_database(weight):
    for elem in weight["weight"]:
        date = dateutil.parser.parse(elem["date"])
        weight = float(elem["weight"]) / 2.204

        new_weight = models.Weight(value=weight, date=date)
        session.add(new_weight)
        try:
            session.commit()
        except IntegrityError as e:
            session.rollback()
            pass


def plot():
    weight = session.query(models.Weight).filter().all()
    dates_x = [elem.date for elem in weight]
    weight_y = [elem.value for elem in weight]

    #dates_x = [dateutil.parser.parse(s) for s in dates_x]

    fig = plt.figure(figsize=(20, 5), dpi = 400, edgecolor='k')
    ax = fig.add_subplot(111)
    ax.set_xticks(dates_x)
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    xfmt = md.DateFormatter('%d-%m')
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


if __name__ == "__main__":

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)

    print('Retrieving the weight...')
    weight = get_bodyweight(today - datetime.timedelta(days=31), today)

    print('Database insertion...')
    insert_database(weight)

    print('Generation of the graph')
    plot() # plot the evolution of the weight with data from the database
