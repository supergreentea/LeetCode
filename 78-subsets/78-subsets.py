class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        def backtrack(index, subset):
            output.append(subset.copy())
            for i in range(index, n):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return output