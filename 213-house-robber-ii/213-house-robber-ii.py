class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        # rob 0 to n - 2
        r1 = r2 = 0
        for i in range(0, n - 1):
            r = max(r1 + nums[i], r2)
            r1, r2 = r2, r
        
        # rob 1 to n - 1
        t1 = t2 = 0
        for i in range(1, n):
            t = max(t1 + nums[i], t2)
            t1, t2 = t2, t
         
        return max(r, t)