class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #time: O(N ^ 2)
        #space: O(N)
        N = len(nums)
        dp = [1] * N
        
        for end in range(1, N):
            for prevEnd in range(end):
                if nums[end] > nums[prevEnd]:
                    dp[end] = max(dp[end], 1 + dp[prevEnd])
        
        return max(dp)