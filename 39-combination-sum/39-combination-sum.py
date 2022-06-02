class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, comb, comb_sum):
            if comb_sum == target:
                res.append(comb.copy())
                return
            
            if i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if comb_sum + candidates[j] > target:
                    continue
                comb.append(candidates[j])
                backtrack(j, comb, comb_sum + candidates[j])
                comb.pop()
        
        backtrack(0, [], 0)
        return res