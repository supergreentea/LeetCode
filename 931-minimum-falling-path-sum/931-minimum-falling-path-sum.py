class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        prev_row = matrix[0].copy()
        
        for row in range(1, ROWS):
            cur_row = matrix[row].copy()
            cur_row[0] += min(prev_row[0], prev_row[1])
            for col in range(1, COLS - 1):
                cur_row[col] += min(prev_row[col-1], prev_row[col], prev_row[col+1])
            cur_row[COLS-1] += min(prev_row[COLS-1], prev_row[COLS-2])
            prev_row = cur_row
        
        return min(prev_row)