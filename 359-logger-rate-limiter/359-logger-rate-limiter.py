class Logger:

    def __init__(self):
        self.timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timestamps and timestamp - self.timestamps[message] < 10:
            return False
        self.timestamps[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)