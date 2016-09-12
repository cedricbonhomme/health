#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from bootstrap import Base

class Weight(Base):
    __tablename__ = 'weight'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    date = Column(DateTime, unique=True, default=datetime.now)
