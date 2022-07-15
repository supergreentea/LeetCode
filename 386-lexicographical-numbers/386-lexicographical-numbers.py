class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        current = 1
        for i in range(1, n + 1):
            res.append(current)
            if current * 10 <= n:
                current *= 10
            elif current % 10 != 9 and current + 1 <= n:
                current += 1
            else:
                while current % 10 == 9 or current == n:
                    current //= 10
                
                current += 1
        return res