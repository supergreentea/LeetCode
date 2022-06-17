class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = white_count = blue_count = 0
        
        for color in nums:
            if color == 0:
                red_count += 1
            elif color == 1:
                white_count += 1
            else:
                blue_count += 1
        
        index = 0
        for _ in range(red_count):
            nums[index] = 0
            index += 1
        for _ in range(white_count):
            nums[index] = 1
            index += 1
        for _ in range(blue_count):
            nums[index] = 2
            index += 1
        
        
        