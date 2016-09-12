#! /usr/bin/env python
# -*- coding: utf-8 -*-

from manager import Manager
from bootstrap import Base

import models

manager = Manager()

@manager.command
def db_create():
    "Will create the database from conf parameters."
    Base.metadata.create_all()


if __name__ == '__main__':
    manager.main()
