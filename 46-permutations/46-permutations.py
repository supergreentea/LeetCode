class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first = 0):
            if first == n:
                output.append(nums.copy())
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output