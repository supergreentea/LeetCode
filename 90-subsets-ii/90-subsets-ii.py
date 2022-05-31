class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        
        def backtrack(start, subset):
            subsets.append(subset.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: # avoid duplicates
                    continue
                
                # backtrack
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        backtrack(0, [])
        return subsets