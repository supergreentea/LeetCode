class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsubarray = subarray = nums[0]
        for i in range(1, len(nums)):
            subarray = max(nums[i] + subarray, nums[i])
            maxsubarray = max(subarray, maxsubarray)
        return maxsubarray