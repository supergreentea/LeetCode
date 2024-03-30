class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        
        for end in range(N):
            for prevEnd in range(end):
                if nums[end] > nums[prevEnd]:
                    dp[end] = max(dp[end], dp[prevEnd] + 1)
        
        return max(dp)
        