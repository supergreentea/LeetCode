class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #time: O(num coins * amount)
        #space: O(amount)
        
        @cache
        def dp(i: int, remaining: int) -> int:
            if i == len(coins) or remaining < 0:
                return 0
            if remaining == 0:
                return 1
            
            coin = coins[i]
            if coin > amount:
                return dp(i + 1, remaining)
            return dp(i + 1, remaining) + dp(i, remaining - coin)
        
        return dp(0, amount)