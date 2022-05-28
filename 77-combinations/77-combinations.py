class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(num, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(num, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res