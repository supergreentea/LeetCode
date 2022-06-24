class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def backtrack(start = 1, comb = []):
            if len(comb) == k:
                output.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack()
        
        return output