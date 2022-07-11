class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = {}, {}, {}
        
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            boxes[i] = set()
        
        box_ranges = {
            0: ((0, 2), (0, 2)),
            1: ((0, 2), (3, 5)),
            2: ((0, 2), (6, 8)),
			3: ((3, 5), (0, 2)),
			4: ((3, 5), (3, 5)),
			5: ((3, 5), (6, 8)),
			6: ((6, 8), (0, 2)),
			7: ((6, 8), (3, 5)),
			8: ((6, 8), (6, 8))
        }
        
        def get_box(row, col):
            for box in range(9):
                min_row, max_row = box_ranges[box][0]
                min_col, max_col = box_ranges[box][1]
                if row >= min_row and row <= max_row and col >= min_col and col <= max_col:
                    return box
            return -1
        
        todo = 0
        
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    digit = str(board[row][col])
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[get_box(row, col)].add(digit)
        
        def backtrack(row, col):
            if row == 9:
                return True
            
            next_row, next_col = (row, col + 1) if col + 1 < 9 else (row + 1, 0)
            
            if board[row][col] != ".":
                return backtrack(next_row, next_col)
            
            box_index = get_box(row, col)
            
            for i in range(1, 10):
                digit = str(i)
                if digit not in rows[row] and digit not in cols[col] and digit not in boxes[box_index]:
                    
                    # place digit
                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[box_index].add(digit)
                    
                    if backtrack(next_row, next_col):
                        return True
                    
                    # remove digit
                    board[row][col] = "."
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[box_index].remove(digit)
            
            return False
        
        backtrack(0, 0)
        
        
         
            