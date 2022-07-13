class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[0] <= nums[-1]:
            return nums[0]
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m - 1] > nums[m]:
                return nums[m]
            
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1