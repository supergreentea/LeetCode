class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        num_candidates = len(candidates)
        
        output = []
        
        def backtrack(index, combination, current_sum):
            if current_sum > target:
                return
            if current_sum == target:
                output.append(combination.copy())
                return
            for i in range(index, num_candidates):
                combination.append(candidates[i])
                backtrack(i, combination, current_sum + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        
        return output