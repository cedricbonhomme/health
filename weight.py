#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
import datetime

import configparser as confparser
config = confparser.SafeConfigParser()
config.read("conf.cfg")
CLIENT_KEY = config.get('oauth', 'CLIENT_KEY')
CLIENT_SECRET = config.get('oauth', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('oauth', 'ACCESS_TOKEN')
REFRESH_TOKEN = config.get('oauth', 'REFRESH_TOKEN')

client_kwargs = {
        'client_id': CLIENT_KEY,
        'client_secret': CLIENT_SECRET,
        'callback_uri': 'https://dev.fitbit.com',
        'scope': ['sleep+settings+nutrition+activity+social+heartrate+profile+weight+location']
}

# fb = fitbit.Fitbit(**client_kwargs)
# retval = fb.client.authorize_token_url()
# print(retval)

fb_client = fitbit.Fitbit(CLIENT_KEY, CLIENT_SECRET,
                        access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


def get_bodyweight(base_date, end_date=None):
    """
    Return data about the body weight.
    """
    weight = fb_client.get_bodyweight(base_date=base_date, end_date=end_date)
    return weight


def plot(weight):
    dates_x = [elem["date"] for elem in weight["weight"]]
    weight_y = [float(elem["weight"])/2.204 for elem in weight["weight"]]

    dates_x = [dateutil.parser.parse(s) for s in dates_x]

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

    weight = get_bodyweight(today - datetime.timedelta(days=30), today)
    print(weight)
    plot(weight)
    """
    for i in range(1):
        weight = get_bodyweight(today - datetime.timedelta(days=i))
        #plot(weight)
        print(weight)"""
