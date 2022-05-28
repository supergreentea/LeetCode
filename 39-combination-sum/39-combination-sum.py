class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, lst, total):
            if total == target:
                res.append(lst.copy())
                return
            elif total > target:
                return
            
            for j in range(i, len(candidates)):
                lst.append(candidates[j])
                backtrack(j, lst, total + candidates[j])
                lst.pop()
        
        backtrack(0, [], 0)
        return res