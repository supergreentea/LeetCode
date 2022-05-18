class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        N = len(nums)
        dp1, dp2 = [None for _ in range(N + 1)], [None for _ in range(N + 1)]
        
        # 0 to N - 2 for dp1
        dp1[N - 1], dp1[N - 2] = 0, nums[N - 2]
        for i in range(N - 3, -1, -1):
            dp1[i] = max(dp1[i + 1], nums[i] + dp1[i + 2])
        
        # 1 to N - 1 for dp2
        dp2[N], dp2[N - 1] = 0, nums[N - 1]
        for i in range(N - 2, 0, -1):
            dp2[i] = max(dp2[i + 1], nums[i] + dp2[i + 2])
        
        return max(dp1[0], dp2[1])