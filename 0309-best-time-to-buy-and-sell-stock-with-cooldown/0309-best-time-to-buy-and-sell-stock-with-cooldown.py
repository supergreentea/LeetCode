class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def maxProfit(index: int = 0, buy: bool = True) -> int:
            if index >= len(prices):
                return 0
            
            cooldown = maxProfit(index + 1, buy)
            if buy:
                buy = maxProfit(index + 1, not buy) - prices[index]
                return max(buy, cooldown)
            sell = maxProfit(index + 2, not buy) + prices[index]
            return max(sell, cooldown)
        
        return maxProfit()