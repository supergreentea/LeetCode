class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        
        x = 1
        for i in range(n // 2):
            res.append(x)
            res.append(-1 * x)
            x += 1
        if n % 2 == 1:
            res.append(0)
        
        return res