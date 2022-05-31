class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        
        def expand(l, r):
            nonlocal start
            nonlocal end
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l-= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[start : end + 1]
        
        