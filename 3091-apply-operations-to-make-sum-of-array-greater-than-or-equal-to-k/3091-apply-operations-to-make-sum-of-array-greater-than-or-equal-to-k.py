class Solution:
    def minOperations(self, k: int) -> int:
        if k <= 1:
            return 0
        
        total = 0
        operations = k
        
        for i in range(k + 1):
            for j in range(k + 1):
                if (1 + i + (1 + i) * j) >= k:
                    operations = min(operations, i + j)
                    break

        return operations