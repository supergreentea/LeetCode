class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # we are on part of array before pivot
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1