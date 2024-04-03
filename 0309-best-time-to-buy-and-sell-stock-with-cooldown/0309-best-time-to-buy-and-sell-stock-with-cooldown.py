class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def maxProfit(index: int = 0, buying: bool = True) -> int:
            if index >= len(prices):
                return 0
            
            cooldown = maxProfit(index + 1, buying)
            if buying:
                buy = maxProfit(index + 1, not buying) - prices[index]
                return max(buy, cooldown)
            sell = maxProfit(index + 2, not buying) + prices[index]
            return max(sell, cooldown)
        
        return maxProfit()