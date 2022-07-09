class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def max_profit(index):
            if index >= len(nums):
                return 0
            if index == len(nums) - 1:
                return nums[index]
            return max(max_profit(index + 2) + nums[index], max_profit(index + 1))
        return max_profit(0)