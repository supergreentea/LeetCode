class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red_index, blue_index = 0, n - 1
        
        for color in nums:
            if color == 0:
                red_index += 1
            elif color == 2:
                blue_index -= 1
        
        for i in range(0, red_index):
            nums[i] = 0
        
        for i in range(red_index, blue_index + 1):
            nums[i] = 1
        
        for i in range(blue_index + 1, n):
            nums[i] = 2