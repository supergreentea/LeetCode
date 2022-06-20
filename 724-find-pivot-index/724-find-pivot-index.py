class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefix_sum = 0
        for i in range(n):
            if (total - nums[i]) / 2 == prefix_sum:
                return i
            prefix_sum += nums[i]
        return -1