#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from precious.sheduler import scheduler
logger = logging.getLogger("scheduler")

if __name__ == '__main__':
    logger.info("Starting sheduler")
    scheduler.start()
    # print('Press Ctrl+C to exit')
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass
