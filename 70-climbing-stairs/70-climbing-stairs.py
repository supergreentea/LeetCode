class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 1, 1
        for k in range(n - 1):
            t = i + j
            i = j
            j = t
        return j