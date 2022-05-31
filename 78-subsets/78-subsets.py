class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        def backtrack(start, subset):
            if start == n:
                subsets.append(subset.copy())
                return
            
            subset.append(nums[start])
            backtrack(start + 1, subset)
            subset.pop()
            backtrack(start + 1, subset)
        
        backtrack(0, [])
        return subsets