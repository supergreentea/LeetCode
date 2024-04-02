class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        
        for end in range(1, N):
            for prevEnd in range(end):
                if nums[end] > nums[prevEnd]:
                    dp[end] = max(dp[end], 1 + dp[prevEnd])
        
        return max(dp)