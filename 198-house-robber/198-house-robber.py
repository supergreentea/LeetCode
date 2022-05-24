class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = nums[len(nums) - 1], 0
        for i in range(len(nums) - 2, -1, -1):
            t = max(nums[i] + rob2, rob1)
            rob1, rob2 = t, rob1
        return rob1