class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, p, used):
            if len(used) == len(nums):
                res.append(p.copy())
                return
            for num in nums:
                if num not in used:
                    used.add(num)
                    p[index] = num
                    backtrack(index + 1, p, used)
                    used.remove(num)
        
        backtrack(0, [0 for _ in range(len(nums))], set())
        return res
                