class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dp(sIndex: int = 0, tIndex: int = 0) -> int:
            if tIndex == len(t):
                    return 1
            if sIndex == len(s):
                return 0
            
            if s[sIndex] == t[tIndex]:
                return dp(sIndex + 1, tIndex + 1) + dp(sIndex + 1, tIndex)
            return dp(sIndex + 1, tIndex)
        
        return dp()