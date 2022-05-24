class Solution:
    def __init__(self):
        self.memo = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        res = math.inf
        for coin in coins:
            p = self.coinChange(coins, amount - coin)
            if p != -1:
                res = min(res, p + 1)
        res = res if res != math.inf else -1    
        self.memo[amount] = res
        return res