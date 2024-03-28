class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ans = []
        
        def backtrack(index: int, combination: List[int], currentSum: int) -> None:
            if currentSum == target:
                ans.append(combination[:])
                return
            if index >= len(candidates) or currentSum > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1, combination, currentSum + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return ans