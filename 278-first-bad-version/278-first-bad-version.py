# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first_bad_version = -1
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                first_bad_version = middle
                right = middle - 1
            else:
                left = middle + 1
        return first_bad_version