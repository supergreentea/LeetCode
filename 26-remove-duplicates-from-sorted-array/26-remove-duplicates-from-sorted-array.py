class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_head = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[write_head] = nums[i]
                write_head += 1
        return write_head