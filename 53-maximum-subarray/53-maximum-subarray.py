class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray = subarray = nums[0]
        for i in range(1, len(nums)):
            subarray = max(nums[i], nums[i] + subarray)
            maxSubarray = max(subarray, maxSubarray)
        return maxSubarray