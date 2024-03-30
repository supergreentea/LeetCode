class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def minCoins(remaining: int = amount) -> int:
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            ans = math.inf
            for coin in coins:
                partialSolution = minCoins(remaining - coin)
                if partialSolution != - 1:
                    ans = min(ans, 1 + partialSolution)
            return ans if ans != math.inf else -1
        
        return minCoins()