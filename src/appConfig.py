# import json module
import json

# initialize the app config global variable
appConf = {}


def loadAppConfig(fName="config/config.json"):
    # load config json into the global variable
    with open(fName) as f:
        global appConf
        appConf = json.load(f)
        return appConf


def getAppConfig():
    # get the cached application config object
    global appConf
    return appConf
