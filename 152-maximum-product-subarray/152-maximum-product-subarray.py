class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time and O(1) memory
        curMin, curMax, res = 1, 1, nums[0]
        
        for n in nums:
            curMax, curMin = max(n * curMax, n * curMin, n), min(n * curMax, n * curMin, n)
            res = max(res, curMax)
        
        return res