class HitCounter:

    def __init__(self):
        self.total = 0
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append((timestamp, 1))
        else:
            timestamp, prev_count = self.hits.pop()
            self.hits.append((timestamp, prev_count + 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.total -= self.hits.popleft()[1]
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)