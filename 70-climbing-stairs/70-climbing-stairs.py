class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        i, j = 1, 2
        for k in range(3, n):
            t = i + j
            i = j
            j = t
        return i + j