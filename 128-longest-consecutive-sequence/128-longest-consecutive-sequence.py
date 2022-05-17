class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in Set:
                length = 1
                while nums[i] + length in Set:
                    length += 1
                longest = max(longest, length)
        return longest