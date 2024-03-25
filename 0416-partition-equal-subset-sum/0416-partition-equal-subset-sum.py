class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        @lru_cache(None)
        def dp(index: int = 0, currentSum: int = 0) -> bool:
            if currentSum == total - currentSum:
                return True
            if currentSum > total - currentSum or index >= len(nums):
                return False
            return dp(index + 1, currentSum) or dp(index + 1, currentSum + nums[index])
        
        return dp()