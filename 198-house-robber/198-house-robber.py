class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = r2 = 0
        for r in nums:
            max_profit = max(r1 + r, r2)
            r1, r2 = r2, max_profit
        return r2