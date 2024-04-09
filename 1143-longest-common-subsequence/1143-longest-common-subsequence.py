class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        
        @cache
        def dp(index1: int = 0, index2: int = 0) -> int:
            if index1 == M or index2 == N:
                return 0
            if text1[index1] == text2[index2]:
                return 1 + dp(index1 + 1, index2 + 1)
            return max(dp(index1 + 1, index2), dp(index1, index2 + 1))
        
        return dp()