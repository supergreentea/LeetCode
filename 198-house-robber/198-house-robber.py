class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None for _ in range(len(nums) + 1)]
        dp[len(nums)], dp[len(nums) - 1] = 0, nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]