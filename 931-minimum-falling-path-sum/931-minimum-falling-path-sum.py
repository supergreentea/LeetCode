class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(1, ROWS):
            matrix[r][0] += min(matrix[r-1][0], matrix[r-1][1]) 
            matrix[r][COLS-1] += min(matrix[r-1][COLS-1], matrix[r-1][COLS-2])
            for c in range(1, COLS - 1):
                matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c], matrix[r-1][c+1])
        return min(matrix[ROWS - 1])