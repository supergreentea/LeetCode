class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [None for _ in range(len(nums) + 1)] # consider houses from 0 to n - 2
        dp2 = [None for _ in range(len(nums) + 1)] # consider houses from 1 to n - 1
        
        N = len(nums)
        
        dp1[N - 1], dp1[N - 2] = 0, nums[N - 2]
        dp2[N], dp2[N - 1] = 0, nums[N - 1] 
        
        for i in range(N - 3, -1, -1):
            dp1[i] = max(nums[i] + dp1[i + 2], dp1[i + 1])
        
        for i in range(N - 2, 0, -1):
            dp2[i] = max(nums[i] +dp2[i + 2], dp2[i + 1])
        
        return max(dp1[0], dp2[1])