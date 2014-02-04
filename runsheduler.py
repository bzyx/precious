#!/usr/bin/env python
# -*- coding: utf-8 -*-

from precious.sheduler import scheduler

if __name__ == '__main__':
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
