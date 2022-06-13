class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(index = 1, comb = []):
            if len(comb) == k:
                output.append(comb.copy())
            for i in range(index, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        output = []
        backtrack()
        return output
        