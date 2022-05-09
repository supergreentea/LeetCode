class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowest:
                maxp = max(maxp, prices[i] - lowest)
            else:
                lowest = prices[i]
        return maxp