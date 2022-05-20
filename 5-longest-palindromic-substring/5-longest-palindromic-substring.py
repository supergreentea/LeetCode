class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        
        def expand(lo, hi): # expand from center(s) until not a palindrome
            nonlocal start
            nonlocal end
            while 0 <= lo and hi < len(s) and s[lo] == s[hi]:
                if hi - lo > end - start:
                    start, end = lo, hi
                lo -= 1
                hi += 1
        
        for i in range(len(s)):
            expand(i, i) # odd palindrome case
            expand(i, i + 1) # even palindrome case
        
        return s[start : end + 1]