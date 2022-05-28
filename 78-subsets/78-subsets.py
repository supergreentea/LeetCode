class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def backtrack(start, subset):
            for i in range(start, len(nums)):
                subset.append(nums[i])
                res.append(subset.copy())
                backtrack(i + 1, subset)
                subset.pop()
                
        backtrack(0, [])
        return res
            