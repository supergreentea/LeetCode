class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def helper(start, subset):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()
        
        helper(0, [])
        return res
            