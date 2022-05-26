class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = max_product = res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            min_product, max_product = min(n * min_product, n * max_product, n), max(n * min_product, n * max_product, n)
            res = max(res, max_product)
        return res