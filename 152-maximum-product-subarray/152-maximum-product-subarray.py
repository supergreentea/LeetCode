class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = max_so_far = ans = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            temp = max(min_so_far * cur, max_so_far * cur, cur)
            min_so_far = min(min_so_far * cur, max_so_far * cur, cur)
            max_so_far = temp
            ans = max(ans, max_so_far)
        return ans
            
        