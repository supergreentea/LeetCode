class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def get_count(index = 0, cur_sum = 0):
            if index == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            return get_count(index + 1, cur_sum + nums[index]) + get_count(index + 1, cur_sum - nums[index])
        
        return get_count()