from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dp(index1: int = 0, index2: int = 0) -> bool:
            if index1 == len(s1) and index2 == len(s2) and index1 + index2 == len(s3):
                return True
            index3 = index1 + index2
            if index1 < len(s1) and s1[index1] == s3[index3] and dp(index1 + 1, index2):
                return True
            if index2 < len(s2) and s2[index2] == s3[index3] and dp(index1, index2 + 1):
                return True
            return False
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        return dp()
