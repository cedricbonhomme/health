#! /usr/bin/env python
# -*- coding: utf-8 -*-

import fitbit

import configparser as confparser
config = confparser.SafeConfigParser()
config.read("conf.cfg")
CLIENT_KEY = config.get('oauth', 'CLIENT_KEY')
CLIENT_SECRET = config.get('oauth', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('oauth', 'ACCESS_TOKEN')
REFRESH_TOKEN = config.get('oauth', 'REFRESH_TOKEN')

ACCESS_REFRESH_TOKEN_URI = "https://api.fitbit.com/oauth2/token"

client_kwargs = {
        'client_id': CLIENT_KEY,
        'client_secret': CLIENT_SECRET,
        'callback_uri': 'https://dev.fitbit.com',
        'scope': ['sleep+settings+nutrition+activity+social+heartrate+profile+weight+location']
}
client_kwargs['access_token'] = ACCESS_TOKEN
client_kwargs['refresh_token'] = REFRESH_TOKEN



fb = fitbit.Fitbit(CLIENT_KEY, CLIENT_SECRET, oauth2=True, access_token='', refresh_token=REFRESH_TOKEN)

print(dir(fb.client))
fb.client.refresh_token()



print(fb.client.token['access_token'])
retval = fb.client.refresh_token()
#print(retval)
