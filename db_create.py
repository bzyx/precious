#!/usr/bin/env python
# -*- coding: utf-8 -*-
from precious import db
from precious.models import *

if __name__ == "__main__":
    db.create_all()

    admin = User(name="admin", password="admin")
    db.session.add(admin)
    db.session.commit()

    p = Project('bla')
    db.session.add(p)
    db.session.commit()

    #import pdb; pdb.set_trace()
