class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] # 0 is start of history
        self.historyEnd = 0 # index of current end of history
        self.curIndex = 0

    def visit(self, url: str) -> None:
        self.curIndex += 1
        self.historyEnd = self.curIndex
        if len(self.history) <= self.historyEnd:
            self.history.append(url)
        else:
            self.history[self.historyEnd] = url

    def back(self, steps: int) -> str:
        self.curIndex = max(0, self.curIndex - steps)
        return self.history[self.curIndex]

    def forward(self, steps: int) -> str:
        self.curIndex = min(self.historyEnd, self.curIndex + steps)
        return self.history[self.curIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)