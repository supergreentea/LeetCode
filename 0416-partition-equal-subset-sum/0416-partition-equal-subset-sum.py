class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        @cache
        def dp(index: int = 0, currentSum: int = 0) -> bool:
            if index >= len(nums):
                return False
            remainingSum = total - currentSum
            if currentSum > remainingSum: 
                return False
            if currentSum == remainingSum:
                return True
            return dp(index + 1, currentSum) or dp(index + 1, currentSum + nums[index])
        
        return dp()