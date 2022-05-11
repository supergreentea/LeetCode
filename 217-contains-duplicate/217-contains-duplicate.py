class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for num in nums:
            if num in Set:
                return True
            Set.add(num)
        return False