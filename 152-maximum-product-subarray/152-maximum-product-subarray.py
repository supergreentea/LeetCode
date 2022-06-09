class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subarray_min = subarray_max = max_product = nums[0]
        for i in range(1, len(nums)):
            subarray_min, subarray_max = min(nums[i] * subarray_min, nums[i] * subarray_max, nums[i]), max(nums[i] * subarray_min, nums[i] * subarray_max, nums[i])
            max_product = max(max_product, subarray_max)
        return max_product
        