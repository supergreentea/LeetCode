class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def getCount(index: int = 0, currentSum: int = 0) -> int:
            if index == len(nums):
                if currentSum == target:
                    return 1
                return 0
            return getCount(index + 1, currentSum + nums[index]) + getCount(index + 1, currentSum - nums[index])
        
        return getCount()