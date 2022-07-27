# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = -1
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                first = m
                r = m - 1
            else:
                l = m + 1
        return first