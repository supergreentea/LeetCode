class Solution:
    
    # O(len(w))
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sums = [0] * len(w)
        self.prefix_sums[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + w[i]
    
    # O(len(w))
    def pickIndex(self) -> int:
        random_number = randint(1, self.prefix_sums[-1])
        low, high = 0, len(self.w)
        while low < high:
            middle = low + (high - low) // 2
            if random_number > self.prefix_sums[middle]:
                low = middle + 1
            else:
                high = middle
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()