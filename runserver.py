#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from precious import app, config
    print config.getint('webserver', 'port')
    app.run(host=config.get('webserver', 'bind'), port=config.getint('webserver', 'port'))