class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #time: O(N * sum of nums)
        #space: O(N) -> max depth of recursion
        
        @cache
        def getCount(index: int, currentSum: int) -> int:
            if index >= len(nums):
                if currentSum == target:
                    return 1
                return 0
            return getCount(index + 1, currentSum + nums[index]) + getCount(index + 1, currentSum - nums[index])
        
        return getCount(0, 0)