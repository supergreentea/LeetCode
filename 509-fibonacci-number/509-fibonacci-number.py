class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for i in range(n - 1):
            c = a + b
            a, b = b, c
        return b
        