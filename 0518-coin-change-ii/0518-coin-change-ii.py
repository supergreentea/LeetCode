class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(index: int = 0, currentAmount: int = 0) -> int:
            if index >= len(coins):
                return 0
            if currentAmount > amount:
                return 0
            if currentAmount == amount:
                return 1
            return dp(index, currentAmount + coins[index]) + dp(index + 1, currentAmount)
        
        return dp()
            