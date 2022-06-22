class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for num in nums:
            if not num - 1 in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                max_length = max(max_length, length)
        
        return max_length
                