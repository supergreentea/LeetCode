class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        def helper(l, r):
            r1, r2 = 0, 0
            for i in range(l, r + 1):
                t = max(r1 + nums[i], r2)
                r1, r2 = r2, t
            return r2
        
        return max(nums[0], helper(0, N - 2), helper(1, N - 1))