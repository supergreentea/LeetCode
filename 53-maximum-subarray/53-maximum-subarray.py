class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for i in range(1, len(nums)):
            current_subarray = max(nums[i], nums[i] + current_subarray)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray