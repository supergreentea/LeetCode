class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(cur_index, combination, total):
            if total > target:
                return
            if total == target:
                res.append(combination.copy())
                return
            for i in range(cur_index, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return res