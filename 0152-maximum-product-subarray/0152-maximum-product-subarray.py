class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        minSoFar = maxSoFar = result = nums[0]
        result = maxSoFar
        for i in range(1, N):
            num = nums[i]
            newMax = max(num, maxSoFar * num, minSoFar * num)
            minSoFar = min(num, maxSoFar * num, minSoFar * num)
            maxSoFar = newMax
            result = max(result, maxSoFar)
        return result
            