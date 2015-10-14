
class OneWayBuffer:

    def __init__(self):
        self.buffer = ""
        self.cursor = 0
        self.version = 0
        self.rLock = False # Read lock

    def add(self, content):
        self.rLock = True
        self.buffer += content
        self.rLock = False

    def clear(self):
        self.rLock = True
        self.buffer = ""
        self.cursor = 0
        self.version += 1
        self.rLock = False

    def readNew(self):
        if self.rLock == True:
            return ""
        # * Read some text
        str = self.buffer[self.cursor:]
        self.cursor = len(self.buffer)
        return str

