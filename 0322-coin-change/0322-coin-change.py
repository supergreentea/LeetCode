class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def fewestCoins(remainingAmount: int = amount) -> int:
            if remainingAmount < 0:
                return -1
            if remainingAmount == 0:
                return 0
            ans = math.inf
            for coin in coins:
                partialSolution = fewestCoins(remainingAmount - coin)
                if partialSolution != -1:
                    ans = min(ans, 1 + partialSolution)
            return ans if ans != math.inf else -1
    
        return fewestCoins()