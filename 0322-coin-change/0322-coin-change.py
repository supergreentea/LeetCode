class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def findFewestCoins(remainingAmount: int = amount) -> int:
            if remainingAmount < 0:
                return -1
            if remainingAmount == 0:
                return 0
            fewest = math.inf
            for coin in coins:
                partialSolution = findFewestCoins(remainingAmount - coin)
                if partialSolution != -1:
                    fewest = min(fewest, 1 + partialSolution)
            return fewest if fewest != math.inf else -1
        
        return findFewestCoins()