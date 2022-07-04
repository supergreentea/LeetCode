class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.deque = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.deque) >= self.size:
            self.total -= self.deque.popleft()
        self.total += val
        self.deque.append(val)
        return self.total / len(self.deque)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)