class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        
        def helper(remain):
            if remain in memo:
                return memo[remain]
            if remain == 0:
                return 0
            num_coins = math.inf
            for coin in coins:
                if remain - coin >= 0 and helper(remain - coin) != -1:
                    num_coins = min(num_coins, helper(remain - coin) + 1)
            num_coins = -1 if num_coins == math.inf else num_coins
            memo[remain] = num_coins
            return num_coins
        
        return helper(amount)
            