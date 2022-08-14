class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        Set = set()
        for num in nums:
            if num in Set:
                return num
            Set.add(num)