class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # O(amount * len(coins)) time complexity
        # O(amount) space complexity 
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
                
        return dp[amount] if dp[amount] != amount + 1 else -1