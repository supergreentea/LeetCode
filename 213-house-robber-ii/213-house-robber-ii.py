class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums, 0, len(nums) - 2), self.helper(nums, 1, len(nums) - 1))
        
    def helper(self, nums, start, end):
        r1, r2 = 0, 0
        for i in range(start, end + 1):
            t = max(r1 + nums[i], r2)
            r1, r2 = r2, t
        return r2