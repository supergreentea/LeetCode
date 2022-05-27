class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, cur, total):
            if total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            for i in range(i, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, cur, total + candidates[i])
                cur.pop()
        backtrack(0, [], 0)
        return res