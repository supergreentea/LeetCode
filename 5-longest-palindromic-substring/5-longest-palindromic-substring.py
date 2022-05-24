class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        
        def expandAroundCenter(low, high):
            nonlocal start
            nonlocal end
            while 0 <= low and high < len(s) and s[low] == s[high]:
                if high - low > end - start:
                    start, end = low, high
                low -= 1
                high += 1
        
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        
        return s[start : end + 1]
                