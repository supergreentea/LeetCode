class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if len(nums) < 2 or total % 2 == 1:
            return False
        
        @cache
        def dp(index: int = 0, currentSum: int = 0) -> bool:
            remaining = total - currentSum
            if index >= len(nums) or currentSum > remaining:
                return False
            if currentSum == remaining:
                return True
            return dp(index + 1, currentSum + nums[index]) or dp(index + 1, currentSum)
        
        return dp()
        
            