class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            m = (l + r) // 2
            square = m * m
            if square < x:
                l = m + 1
            elif square > x:
                r = m - 1
            else:
                return m
        return r