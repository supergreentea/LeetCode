class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red_end, blue_start = 0, n
        
        for color in nums:
            if color == 0:
                red_end += 1
            elif color == 2:
                blue_start -= 1
        
        for i in range(0, red_end):
            nums[i] = 0
        
        for i in range(red_end, blue_start):
            nums[i] = 1
        
        for i in range(blue_start, n):
            nums[i] = 2