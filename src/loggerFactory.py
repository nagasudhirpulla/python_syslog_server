import logging
from logging.handlers import TimedRotatingFileHandler
from logging import LoggerAdapter
import os
import zipfile
from os.path import basename

def rotator(source, dest):
    zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED).write(source, basename(source))
    os.remove(source)


def getFileLogger(name: str, fPath: str, backupCount: int, numRollingHrs: int) -> LoggerAdapter:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # streamHandler = logging.StreamHandler()
    fileHandler = TimedRotatingFileHandler(
        fPath, backupCount=backupCount, when='h', interval=numRollingHrs)
    fileHandler.namer = lambda name: name.replace(".log", "") + ".zip"
    fileHandler.rotator = rotator
    streamFormatter = logging.Formatter("%(message)s")
    # streamHandler.setFormatter(streamFormatter)
    fileHandler.setFormatter(streamFormatter)
    # logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    loggerAdapter = logging.LoggerAdapter(logger, extra={})
    return loggerAdapter
