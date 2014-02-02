#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
from precious.utils import get_logger_config_file_path
from precious.worker import Worker


def configure_logging_worker():
    logging.config.fileConfig(get_logger_config_file_path())


if __name__ == "__main__":
    configure_logging_worker()

    logger = logging.getLogger("worker")
    logger.info("TEST@")
    worker = Worker()
    worker.main()
