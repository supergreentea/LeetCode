class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def helper(nums, i, memo):
            if i > len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            robHere = nums[i] + helper(nums, i + 2, memo)
            dontRobHere = helper(nums, i + 1, memo)
            maxmoney = max(robHere, dontRobHere)
            memo[i] = maxmoney
            return maxmoney
        
        return helper(nums, 0, memo)