class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in Set:
                length = 1
                while n + length in Set:
                    length += 1
                longest = max(longest, length)
        return longest