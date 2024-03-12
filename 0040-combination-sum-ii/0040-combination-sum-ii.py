class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        
        def backtrack(index: int = 0, combination: List[int] = [], currentSum: int = 0):
            if currentSum > target:
                return
            if currentSum == target:
                combinations.append(combination[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1, combination, currentSum + candidates[i])
                combination.pop()
        
        backtrack()
        return combinations
        