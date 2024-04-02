class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        @cache
        def partition(index: int = 0, currentSum: int = 0) -> bool:
            if index >= len(nums):
                return False
            remainingSum = total - currentSum
            if currentSum == remainingSum:
                return True
            return partition(index + 1, currentSum + nums[index]) or partition(index + 1, currentSum)
        
        return partition()