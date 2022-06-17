class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        
        def backtrack(index, subset):
            output.append(subset.copy())
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
                
        backtrack(0, [])
        
        return output
                