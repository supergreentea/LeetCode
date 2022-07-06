class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(index, comb, cur_sum):
            if cur_sum == target:
                output.append(comb.copy())
            if cur_sum > target:
                return
            
            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, cur_sum + candidates[i])
                comb.pop()
        
        backtrack(0, [], 0)
        
        return output