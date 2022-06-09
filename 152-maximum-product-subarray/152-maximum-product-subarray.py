class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subarray_min = subarray_max = max_product = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], subarray_max * nums[i], subarray_min * nums[i])
            subarray_min = min(nums[i], subarray_max * nums[i], subarray_min * nums[i])
            subarray_max = temp
            max_product = max(max_product, subarray_max)
        return max_product
        