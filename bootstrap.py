#! /usr/bin/env python
# -*- coding: utf-8 -*-

import conf
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(conf.DB_URL)

Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()
