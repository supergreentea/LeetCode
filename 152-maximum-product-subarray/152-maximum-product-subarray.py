class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            curMax, curMin = max(n * curMax, n * curMin, n), min(n * curMax, n * curMin, n)
            res = max(res, curMax)
        return res