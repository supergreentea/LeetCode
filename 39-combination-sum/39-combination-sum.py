class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(index = 0, comb = [], comb_sum = 0):
            if comb_sum == target:
                output.append(comb.copy())
            if comb_sum > target:
                return
            
            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, comb_sum + candidates[i])
                comb.pop()
        
        backtrack()
        return output