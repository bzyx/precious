#!/usr/bin/env python
# -*- coding: utf-8 -*-
from precious import db
from precious.models import *

from precious.plugins.git import Git
from precious.plugins.custom_commands import Custom_commands

if __name__ == "__main__":
    db.create_all()

    admin = User(name="admin", password="admin")
    db.session.add(admin)
    db.session.commit()

    p1 = Project(u"Precious CI", u"Python Continuous Integration Server")
    p2 = Project(u"Jenkins", u"Java Suks")
    p3 = Project(u"New project", u"Just an empty project")

    p1.history.append(Build(p1.id, "6597bfe8f42c02a4f2f6269bee71036081b7dc72", u"some stdout\n", True))
    p1.history.append(Build(p1.id, "6597bfe8f42c02a4f2f6269bee71036081b7dc72", u"some stdout1\n", True))
    p1.history.append(Build(p1.id, "6597bfe8f42c02a4f2f6269bee71036081b7dc72", u"some stdout2\n", False))
    p1.history.append(Build(p1.id, "6597bfe8f42c02a4f2f6269bee71036081b7dc72", u"some stdout3\n", True))
    p1.build_steps.append(Git(repo="git@github.com:bzyx/precious.git", branch="master"))
    p1.build_steps.append(Custom_commands(text="git status\nls -al"))

    p2.history.append(Build(p2.id, "rev1", u"some stdout\n", False))

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    #import pdb; pdb.set_trace()
