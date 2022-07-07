class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def count_ways(index = 0, remaining_sum = target):
            if index == len(nums):
                if remaining_sum == 0:
                    return 1
                return 0
            
            return count_ways(index + 1, remaining_sum + nums[index]) + count_ways(index + 1, remaining_sum - nums[index])
        
        return count_ways()