class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        r1 = r2 = 0
        for i in range(len(nums) - 1):
            r = max(r1 + nums[i], r2)
            r1, r2 = r2, r
        
        s1 = s2 = 0
        for i in range(1, len(nums)):
            s = max(s1 + nums[i], s2)
            s1, s2 = s2, s
        
        return max(r2, s2)