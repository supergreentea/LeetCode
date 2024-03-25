class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        @lru_cache(None)
        def backtrack(index: int = 0, currentSum: int = 0) -> bool:
            if currentSum == total - currentSum:
                return True
            if currentSum > total - currentSum or index >= len(nums):
                return False
            return backtrack(index + 1, currentSum) or backtrack(index + 1, currentSum + nums[index])
        
        return backtrack()