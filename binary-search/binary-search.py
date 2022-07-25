class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
        return -1