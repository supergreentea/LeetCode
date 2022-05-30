class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subarray_min = subarray_max = 1
        res = nums[0]
        for n in nums:
            subarray_min, subarray_max = min(subarray_min * n, subarray_max * n, n), max(subarray_min * n, subarray_max * n, n)
            res = max(res, subarray_max)
        return res