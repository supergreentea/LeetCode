class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for row in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[m-1][n-1]