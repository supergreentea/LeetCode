class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sums = [0] * len(w)
        self.prefix_sums[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + w[i]

    def pickIndex(self) -> int:
        random_number = randint(1, self.prefix_sums[-1])
        for i in range(len(self.w)):
            if random_number <= self.prefix_sums[i]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()