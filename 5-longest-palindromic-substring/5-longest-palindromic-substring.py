class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        
        def expand(lo, hi):
            nonlocal start
            nonlocal end
            while 0 <= lo and hi < len(s) and s[lo] == s[hi]:
                if hi - lo > end - start:
                    start, end = lo, hi
                lo -= 1
                hi += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[start : end + 1]