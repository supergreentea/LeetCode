class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 0, 1
        for _ in range(n):
            t = i + j
            i = j
            j = t
        return j