class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(index: int = 0, buying: bool = True) -> int:
            if index >= len(prices):
                return 0
            cooldown = dp(index + 1, buying)
            if buying:
                buy = dp(index + 1, not buying) - prices[index]
                return max(buy, cooldown)
            sell = dp(index + 2, not buying) + prices[index]
            return max(sell, cooldown)
        
        return dp()