class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_length = max_length = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                cur_length = 0
        return max_length