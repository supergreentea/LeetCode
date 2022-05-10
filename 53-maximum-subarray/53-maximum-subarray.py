class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsubarray = subarray = nums[0]
        for i in range(1, len(nums)):
            subarray = max(nums[i], nums[i] + subarray)
            maxsubarray = max(maxsubarray, subarray)
        return maxsubarray