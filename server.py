"""
Syslog Server for collecting logs
and saving in a rolling time log files
"""
import socketserver
from src.loggerFactory import getFileLogger
from src.appConfig import loadAppConfig

appConfig = loadAppConfig()

logFilePath = appConfig["logFilePath"]
HOST, PORT = appConfig["host"], appConfig["port"]
backUpCount = appConfig["backUpCount"]
fileRollingHrs = appConfig["fileRollingHrs"]

logger = getFileLogger(
    "app_logger", logFilePath, backUpCount, fileRollingHrs)


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        strData = str(data)
        # print("%s : " % self.client_address[0], strData)
        # check if data has  type="traffic" and  subtype="forward"
        isTraffic = " type=\"traffic\" "
        isForwardTraffic = " subtype=\"forward\" "
        if isTraffic and isForwardTraffic:
            logger.info(strData)


if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")
