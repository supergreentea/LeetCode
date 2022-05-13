class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        dp[N], dp[N - 1] = 0, nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        
        return dp[0]
        
        