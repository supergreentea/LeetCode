class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        
        if len(nums) == 1:
            return 0
        
        def is_peak(index):
            if index == 0:
                return nums[index] > nums[index + 1]

            if index == len(nums) - 1:
                return nums[index] > nums[index - 1]
            
            return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]
        
        while l < r:
            m = (l + r) // 2
            if is_peak(m):
                return m
            elif nums[m] > nums[m - 1]:
                l = m + 1
            else:
                r = m
        
        return l