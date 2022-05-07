class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in Set:
                length = 0
                while num + length in Set:
                    length += 1
                longest = max(longest, length)
        return longest
                