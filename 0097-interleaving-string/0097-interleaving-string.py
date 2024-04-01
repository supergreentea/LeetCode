class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        @cache
        def dp(s1_index: int, s2_index: int) -> bool:
            s3_index = s1_index + s2_index
            if s3_index == len(s3):
                return True
            for i in range(s1_index, len(s1)):
                if s1[s1_index : i + 1] == s3[s3_index: s3_index +  (i - s1_index) + 1]:
                    if dp(i + 1, s2_index):
                        return True
            for i in range(s2_index, len(s2)):
                if s2[s2_index : i + 1] == s3[s3_index: s3_index +  (i - s2_index) + 1]:
                    if dp(s1_index, i + 1):
                        return True
            return False
        
        return dp(0, 0)