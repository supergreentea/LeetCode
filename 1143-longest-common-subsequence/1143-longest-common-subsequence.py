class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #time: O(M * N)
        #space: O(M * N)
        
        M, N = len(text1), len(text2)
        
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for row in range(M - 1, -1, -1):
            for col in range(N - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col  + 1])
        
        return dp[0][0]
        
                    
                
            