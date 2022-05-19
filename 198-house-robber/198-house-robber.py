class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            t = max(rob1 + nums[i], rob2)
            rob1, rob2 = rob2, t
        return rob2