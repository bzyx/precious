import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler


from utils.utils import get_logs_directory


class logging_writer(object):
    def __init__(self,desc):
        self.desc = desc
    def write(self, data):
        logging.getLogger().info("[%s]%r" % (self.desc,data))


def init():
    handler = TimedRotatingFileHandler(dafix_log, when='w0',backupCount=10)
    logg = logging.getLogger()
    logg.addHandler(handler)
    logg.setLevel(logging.DEBUG)

    fmt = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M')
    handler.setFormatter(fmt)
    logging.captureWarnings(True)
