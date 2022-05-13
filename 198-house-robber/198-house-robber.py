class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def helper(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            robHere = nums[i] + helper(i + 2)
            skipHere = helper(i + 1)
            maxMoney = max(robHere, skipHere)
            memo[i] = maxMoney
            return maxMoney
        
        return helper(0)