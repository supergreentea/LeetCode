from typing import List
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(remaining: int, index: int = 0) -> int:
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            if index == len(coins):
                return 0
            combinations = 0
            # Use the current coin
            combinations += dp(remaining - coins[index], index)
            # Skip the current coin
            combinations += dp(remaining, index + 1)
            return combinations
                    
        return dp(amount)
