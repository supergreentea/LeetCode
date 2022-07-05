class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        
        row = col = 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        VISITED = 101
        
        
        output = [matrix[0][0]]
        matrix[0][0] = VISITED
        
        while len(output) < ROWS * COLS:
            row_offset, col_offset = directions[direction]
            next_row, next_col = row + row_offset, col + col_offset
            if next_row < 0 or next_row >= ROWS or next_col < 0 or next_col >= COLS or matrix[next_row][next_col] == VISITED:
                direction = (direction + 1) % 4
            else:
                output.append(matrix[next_row][next_col])
                matrix[next_row][next_col] = VISITED
                row, col = next_row, next_col
        
        return output