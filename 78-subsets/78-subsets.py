class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def backtrack(index = 0, subset = []):
            output.append(subset.copy())
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack()
        return output