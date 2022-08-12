class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        window_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if window_sum < 0:
                window_sum = nums[i]
            else:
                window_sum += nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum