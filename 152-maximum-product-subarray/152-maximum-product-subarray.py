class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time and O(1) memory
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            curMax, curMin = max(n * curMax, n * curMin, n), min(n * curMax, n * curMin, n)
            res = max(res, curMax)
        
        return res