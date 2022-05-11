class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        maxlength = 0
        for num in nums:
            if num - 1 not in Set:
                length = 1
                while num + length in Set:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength