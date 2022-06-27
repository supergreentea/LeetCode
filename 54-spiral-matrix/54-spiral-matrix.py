class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ROWS, COLS = len(matrix), len(matrix[0])
        NUM_ELEMENTS = ROWS * COLS
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        
        row, col = 0, 0
        output = [matrix[0][0]]
        matrix[0][0] = '#'
        
        while len(output) < NUM_ELEMENTS:
            row_offset, col_offset = directions[direction]
            next_row, next_col = row + row_offset, col + col_offset
            if next_row < 0 or next_row >= ROWS or next_col < 0 or next_col >= COLS or matrix[next_row][next_col] == '#':
                direction = (direction + 1) % 4
            else:
                output.append(matrix[next_row][next_col])
                matrix[next_row][next_col] = '#'
                row, col = next_row, next_col
        
        return output