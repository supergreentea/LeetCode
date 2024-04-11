class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        maxSoFar = minSoFar = nums[0]
        
        maxProduct = maxSoFar
        
        for i in range(1, N):
            num = nums[i]
            newMax = max(num, maxSoFar * num, minSoFar * num)
            minSoFar = min(num, maxSoFar * num, minSoFar * num)
            maxSoFar = newMax
            maxProduct = max(maxProduct, newMax)
        
        return maxProduct