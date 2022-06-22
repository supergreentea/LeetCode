class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for row in range(1, ROWS):
            matrix[row][0] += min(matrix[row-1][0], matrix[row-1][1])
            for col in range(1, COLS - 1):
                matrix[row][col] += min(matrix[row-1][col-1], matrix[row-1][col], matrix[row-1][col+1])
            matrix[row][COLS-1] += min(matrix[row-1][COLS-1], matrix[row-1][COLS-2])
        
        return min(matrix[ROWS-1])