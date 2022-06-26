class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        output = []
        
        def add_diagonal(start, end, increment):
            row, col = start
            while ((row, col) != end):
                output.append(mat[row][col])
                row -= increment
                col += increment
            output.append(mat[row][col])
        
        go_top_right = True
        left = right = top = bottom = 0
        
        while len(output) < ROWS * COLS:
            if go_top_right:
                add_diagonal((bottom, left), (top, right), 1)
            else:
                add_diagonal((top, right), (bottom, left), -1)
            
            if right < COLS - 1:
                right += 1
            else:
                top += 1
            if bottom < ROWS - 1:
                bottom += 1
            else:
                left += 1
            
            go_top_right = not go_top_right
                    
        return output
                