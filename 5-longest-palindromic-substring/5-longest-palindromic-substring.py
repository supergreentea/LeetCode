class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        
        def expand_around_center(i, j):
            nonlocal start
            nonlocal end
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if end - start < j - i:
                    start, end = i, j
                i -= 1
                j += 1
        
        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        
        return s[start : end + 1]