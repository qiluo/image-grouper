class Logger(object):
    """Simple Logger"""
    def __init__(self, level):
        super(Logger, self).__init__()
        self.level = level

    def info(self, info):
        if self.level:
            print info

    def error(self, errMsg):
        print errMsg
