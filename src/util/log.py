# encoding=utf-8

import logging
import os
from datetime import datetime
# from threading import RLock
from multiprocessing import RLock

log_level = logging.DEBUG
MAX_LOG_NUM = 1000000

# log section
if os.name == 'nt':
    DEFAULT_LOG_PATH = 'C:\\searchlog'
else:
    DEFAULT_LOG_PATH = os.path.join('..', 'log')


def createDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


class Log(object):

    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s')

    def __init__(self, loggerName='dip-svc',
                 nameTail=None, logPath=None, debug=False, textHeader=''):
        self.nameTail = nameTail if nameTail\
            else datetime.now().strftime('%Y%m%d-%H%M%S')
        # create log directory
        self.logPath = logPath if logPath else DEFAULT_LOG_PATH
        createDir(self.logPath)

        self.logCount = 0
        self.logFileCount = 0
        logFile = self.logPath + os.sep + 'log-' + self.nameTail + \
            '-%s' % self.logFileCount
        # log handler
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(log_level)
        self.handler = logging.FileHandler(logFile)
        self.handler.setFormatter(Log.formatter)
        self.logger.addHandler(self.handler)
        if debug:
            self.logger.addHandler(logging.StreamHandler())
        self.textHeader = textHeader
        # locker
        self.lock = RLock()

    def addHeader(self, subheader):
        self.textHeader += ' {0} '.format(subheader)

    # log function
    def record(self, text, logFunc=None):
        with self.lock:
            if logFunc:
                logFunc(self.textHeader + text)
                self.checkUpdateHandler()

    def info(self, text):
        self.record(text, self.logger.info)

    def debug(self, text):
        self.record(text, self.logger.debug)

    def warning(self, text):
        self.record(text, self.logger.warning)

    def error(self, text):
        self.record(text, self.logger.error)

    def critical(self, text):
        self.record(text, self.logger.critical)

    def exception(self, text):
        self.record(text, self.logger.exception)

    def checkUpdateHandler(self):
        self.logCount += 1
        if self.logCount >= MAX_LOG_NUM:
            self.logFileCount += 1
            logFile = self.logPath + os.sep + 'log-' + self.nameTail + \
                '-%s' % self.logFileCount
            self.logger.removeHandler(self.handler)
            self.handler = logging.FileHandler(logFile)
            self.handler.setFormatter(Log.formatter)
            self.logger.addHandler(self.handler)
            self.logCount = 0


logger = Log(nameTail='dip-svc')


if __name__ == '__main__':
    # loggerName 是日志名称，不同的日志名称会分别记录
    # nameTail 是日志文件名的后缀，便于区分不同的日志文件
    # logPath 是日志文件的存储路径
    # debug 如果是True，除了记录在文件还会打印到屏幕上
    # logger = Log(loggerName='test1', nameTail='test', logPath='/tmp/testlog')
    logger = Log(nameTail='sender')
    logger.info('this is a info test')
    logger.error('this is a error test')
    logger.warning('this is a warning test')
