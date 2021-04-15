import unittest
from src.appConfig import loadAppConfig
from src.loggerFactory import getFileLogger
import datetime as dt

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.appConfig = loadAppConfig()

    def test_run(self) -> None:
        """tests the app logger
        """
        LOG_FILE = "logs/test.log"
        backUpCount = self.appConfig["backUpCount"]
        fileRollingHrs = self.appConfig["fileRollingHrs"]
        logger = getFileLogger(
            "app_logger", LOG_FILE, backUpCount, fileRollingHrs)
        logger.info("test_{0}".format(dt.datetime.now()))
        self.assertTrue(True)