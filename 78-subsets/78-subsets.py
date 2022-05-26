class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            helper(i + 1, path)
            
            path.append(nums[i])
            helper(i + 1, path)
            path.pop()
        
        helper(0, [])
        
        return res