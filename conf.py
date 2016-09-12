#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser as confparser

config = confparser.SafeConfigParser()

config.read("conf.cfg")

CLIENT_KEY = config.get('oauth', 'CLIENT_KEY')
CLIENT_SECRET = config.get('oauth', 'CLIENT_SECRET')
ACCESS_TOKEN = config.get('oauth', 'ACCESS_TOKEN')
REFRESH_TOKEN = config.get('oauth', 'REFRESH_TOKEN')

DB_URL = config.get('database', 'database_url')
