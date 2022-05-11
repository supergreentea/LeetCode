class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                profit = prices[i] - lowest
                maxp = max(profit, maxp)
        return maxp