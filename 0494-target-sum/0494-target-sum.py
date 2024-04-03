class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        
        @cache
        def dp(index: int = 0, currentSum: int = 0) -> int:
            nonlocal count
            if index == len(nums):
                if currentSum == target:
                    return 1
                return 0
            add = dp(index + 1, currentSum + nums[index])
            subtract = dp(index + 1, currentSum - nums[index])
            return add +  subtract
        
        return dp()
            