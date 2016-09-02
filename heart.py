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

authd_client = fitbit.Fitbit(CLIENT_KEY, CLIENT_SECRET,
                        access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


def get_intraday_time_series(date, detail_level='1min'):
    """
    Return the heart activity.
    """
    heart_activity = authd_client.intraday_time_series(resource= 'activities/heart',
                                                    base_date=date,
                                                    detail_level = detail_level)
    return heart_activity


def plot(heart_activity):
    beats = heart_activity["activities-heart-intraday"]["dataset"]
    dates_x = [elem["time"] for elem in beats]
    beats_y = [elem["value"] for elem in beats]

    dates_x_less = [elem for index, elem in enumerate(dates_x) if index%10==0]
    beats_y_less = [elem for index, elem in enumerate(beats_y) if index%10==0]

    dates_x = [dateutil.parser.parse(s) for s in dates_x_less]

    fig = plt.figure(figsize=(30, 5), dpi = 400, edgecolor='k')
    ax = fig.add_subplot(111)
    ax.set_xticks(dates_x)
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

    plt.plot(dates_x, beats_y_less, "o-")

    plt.savefig(current_date+'-heart.png', dpi=400, bbox_inches='tight')
    #plt.show()
    plt.clf()


if __name__ == "__main__":

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)

    for i in range(3):
        heart_activity = \
                get_intraday_time_series(today - datetime.timedelta(days=i))
        plot(heart_activity)
