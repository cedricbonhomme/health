#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit
import datetime
import dateutil
from sqlalchemy.exc import IntegrityError

import conf
import models
from bootstrap import session

fb_client = fitbit.Fitbit(conf.CLIENT_KEY, conf.CLIENT_SECRET,
                                access_token=conf.ACCESS_TOKEN,
                                refresh_token=conf.REFRESH_TOKEN)

def retrieve_intraday_time_series(date, detail_level='1min'):
    """
    Retrieve data about the heart.
    """
    heart_activity = fb_client.intraday_time_series(resource= 'activities/heart',
                                                    base_date=date,
                                                    detail_level = detail_level)
    for elem in heart_activity["activities-heart-intraday"]["dataset"]:
        date = datetime.datetime.combine(date,
                                    dateutil.parser.parse(elem["time"]).time())
        value = float(elem["value"])

        new_bpm = models.Heart(value=value, date=date)
        session.add(new_bpm)
        try:
            session.commit()
        except IntegrityError as e:
            session.rollback()
            pass

def retrieve_bodyweight(base_date, end_date):
    """
    Retrieve data about the body weight.
    """
    weight = fb_client.get_bodyweight(base_date=base_date, end_date=end_date)
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
