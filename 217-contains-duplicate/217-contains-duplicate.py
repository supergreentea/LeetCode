class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for n in nums:
            if n in Set:
                return True
            Set.add(n)
        return False