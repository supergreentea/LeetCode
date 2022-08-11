class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_head = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_head] = nums[i]
                write_head += 1
        for i in range(write_head, len(nums)):
            nums[i] = 0