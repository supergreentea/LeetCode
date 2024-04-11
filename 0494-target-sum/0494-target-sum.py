class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        
        @cache
        def dp(i: int = 0, currentSum: int = 0) -> int:
            if i == N:
                if currentSum == target:
                    return 1
                return 0
            return dp(i + 1, currentSum + nums[i]) + dp(i + 1, currentSum - nums[i])
        
        return dp()