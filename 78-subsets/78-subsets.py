class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            helper(i + 1, subset)
            subset.pop()
            helper(i + 1, subset)
        
        helper(0, [])
        return res