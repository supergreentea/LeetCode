class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cur_row = matrix[0].copy()
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(1, ROWS):
            next_row = matrix[row].copy()
            for col in range(COLS):
                if col == 0:
                    next_row[col] += min(cur_row[0], cur_row[1])
                elif col == COLS - 1:
                    next_row[col] += min(cur_row[COLS - 1], cur_row[COLS - 2])
                else:
                    next_row[col] += min(cur_row[col - 1], cur_row[col], cur_row[col + 1])
            cur_row = next_row
        
        return min(cur_row)
        
        