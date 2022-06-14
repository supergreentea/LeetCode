class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(1, ROWS):
            for c in range(COLS):
                if c == 0:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c == COLS - 1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1], matrix[r-1][c-1])
        return min(matrix[-1])