class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def expand(low, high):
            nonlocal res
            while 0 <= low and high < len(s) and s[low] == s[high]:
                res += 1
                low -= 1
                high += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return res
            
                