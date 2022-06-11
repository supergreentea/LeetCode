class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        if nums[l] < nums[r] or len(nums) == 1:
            return nums[0]
        
        while l <= r:
            m = (l + r) // 2
            
            middle = nums[m]
            before_middle = nums[m - 1]
            after_middle = nums[m + 1]
            if nums[m - 1] > nums[m]:
                return nums[m]
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            
            # before pivot
            if nums[0] < nums[m]:
                l = m + 1
            else:
            # after pivot
                r = m - 1
        