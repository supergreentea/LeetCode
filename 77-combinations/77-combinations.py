class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start, comb):
            if len(comb) == k:
                output.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        output = []
        backtrack(1, [])
        return output
                