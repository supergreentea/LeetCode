class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        def backtrack(index, subset):
            if index == n:
                output.append(subset.copy())
                return
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)
        
        backtrack(0, [])
        return output