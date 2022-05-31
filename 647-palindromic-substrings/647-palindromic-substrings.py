class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def expand(i, j):
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
                
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return res