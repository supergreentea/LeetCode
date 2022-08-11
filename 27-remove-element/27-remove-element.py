class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_head = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_head] = nums[i]
                write_head += 1
        return write_head