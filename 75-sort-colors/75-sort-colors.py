class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_zero = cur = 0
        next_two = len(nums) - 1
        
        while cur <= next_two:
            if nums[cur] == 0:
                nums[cur], nums[next_zero] = nums[next_zero], nums[cur]
                cur += 1
                next_zero += 1
            elif nums[cur] == 2:
                nums[cur], nums[next_two] = nums[next_two], nums[cur]
                next_two -= 1
            else:
                cur += 1
                