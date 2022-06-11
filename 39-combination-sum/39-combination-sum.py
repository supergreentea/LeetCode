class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(index, comb, comb_sum):
            if comb_sum == target:
                res.append(comb.copy())
                return
            if index == n or comb_sum > target:
                return
            for i in range(index, n):
                comb.append(candidates[i])
                backtrack(i, comb, comb_sum + candidates[i])
                comb.pop()
        
        backtrack(0, [], 0)
        return res