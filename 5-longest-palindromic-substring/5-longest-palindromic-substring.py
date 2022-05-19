class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart, resEnd = 0, 0
        
        def expand(left, right):
            nonlocal resStart
            nonlocal resEnd
            l, r = left, right
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l > resEnd - resStart:
                    resStart, resEnd = l, r
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[resStart : resEnd + 1]
            
            