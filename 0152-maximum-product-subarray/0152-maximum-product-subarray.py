class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        maxSoFar = minSoFar = nums[0]
        
        maxProduct = maxSoFar
        
        for i in range(1, len(nums)):
            newMax = max(nums[i], maxSoFar * nums[i], minSoFar * nums[i])
            minSoFar = min(nums[i], maxSoFar * nums[i], minSoFar * nums[i])
            maxSoFar = newMax
            maxProduct = max(maxProduct, newMax)
        
        return maxProduct
        