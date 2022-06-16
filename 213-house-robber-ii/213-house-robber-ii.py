"""
Time complexity: O(N) where N is |nums|
Space complexity: O(1) no extra space

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1 = r2 = 0
        n = len(nums)
        for i in range(n - 1):
            r = max(r1 + nums[i], r2)
            r1, r2 = r2, r
        s1 = s2 = 0
        for i in range(1, n):
            s = max(s1 + nums[i], s2)
            s1, s2 = s2, s
        return max(r, s)