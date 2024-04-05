class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def profit(day: int = 0, buying: bool = True) -> int:
            if day >= len(prices):
                return 0
            skip = profit(day + 1, buying)
            if buying:
                buy = profit(day + 1, not buying) - prices[day]
                return max(buy, skip)
            sell = profit(day + 2, not buying) + prices[day]
            return max(skip, sell)
        
        return profit()