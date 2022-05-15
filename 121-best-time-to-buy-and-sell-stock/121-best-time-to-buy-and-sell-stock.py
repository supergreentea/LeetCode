class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxp = 0
        for i in range(1, len(prices)):
            if prices[i] > lowestPrice:
                maxp = max(maxp, prices[i] - lowestPrice)
            else:
                lowestPrice = prices[i]
        return maxp