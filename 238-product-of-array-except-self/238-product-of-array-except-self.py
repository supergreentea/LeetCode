class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        prefix_product = 1
        
        for i in range(len(nums)):
            products[i] = prefix_product
            prefix_product *= nums[i]
        
        suffix_product = 1
        for i in reversed(range(len(nums))):
            products[i] *= suffix_product
            suffix_product *= nums[i]
        
        return products