class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            t = max(nums[i] + rob1, rob2)
            rob1, rob2 = rob2, t
        return rob2