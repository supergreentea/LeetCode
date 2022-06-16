class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            # check if num can be start of a consecutive sequence
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                max_length = max(max_length, length)
        return max_length