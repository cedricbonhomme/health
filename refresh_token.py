#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit

import conf

"""
ACCESS_REFRESH_TOKEN_URI = "https://api.fitbit.com/oauth2/token"

client_kwargs = {
        'client_id': conf.CLIENT_KEY,
        'client_secret': conf.CLIENT_SECRET,
        'callback_uri': 'http://dev.fitbit.com',
        'scope': ['sleep+settings+nutrition+activity+social+heartrate+profile+weight+location']
}
client_kwargs['access_token'] = conf.ACCESS_TOKEN
client_kwargs['refresh_token'] = conf.REFRESH_TOKEN

fb = fitbit.Fitbit(conf.CLIENT_KEY, conf.CLIENT_SECRET, oauth2=True,
                    access_token=conf.ACCESS_TOKEN,
                    refresh_token=conf.REFRESH_TOKEN)

#print(fb.client.token['access_token'])
retval = fb.client.refresh_token()
print(retval)
"""


userid = conf.CLIENT_KEY
REFRESH_TOKEN = conf.REFRESH_TOKEN
ACCESS_TOKEN = conf.ACCESS_TOKEN

authd_client = fitbit.Fitbit(conf.CLIENT_KEY, conf.CLIENT_SECRET, oauth2=True,
                        access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

mystring = str(authd_client.client.refresh_token())
REFRESH_TOKEN = authd_client.client.token['refresh_token']
ACCESS_TOKEN = authd_client.client.token['access_token']
user_id = authd_client.client.token['user_id']
#print (authd_client.client.token['refresh_token'])
print(REFRESH_TOKEN)
print(ACCESS_TOKEN)
print(authd_client)
