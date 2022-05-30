class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]
        return num_paths[m-1][n-1]