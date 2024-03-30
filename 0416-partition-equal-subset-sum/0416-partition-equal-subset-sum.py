class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # O(m * n) for both time and space
        # m is subset sum and n is number of elements in array
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        @cache
        def dp(index: int = 0, currentSum: int = 0) -> bool:
            if index == len(nums):
                return False
            remainingSum = total - currentSum
            if currentSum > remainingSum:
                return False
            if currentSum == remainingSum:
                return True
            return dp(index + 1, currentSum + nums[index]) or dp(index + 1, currentSum)
        
        return dp()