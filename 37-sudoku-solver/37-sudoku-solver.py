class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def get_box(row, col):
            return (row // 3) * 3 + (col // 3)
        
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit.isdigit():
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[get_box(row, col)].add(digit)
        
        def backtrack(row, col):
            if row == 9:
                return True
            
            next_row, next_col = (row, col + 1) if col + 1 < 9 else (row + 1, 0) 
            
            if board[row][col].isdigit():
                return backtrack(next_row, next_col)
            
            box = get_box(row, col)
            
            for i in range(1, 10):
                digit = str(i)
                if digit not in rows[row] and digit not in cols[col] and digit not in boxes[box]:
                    
                    # place digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[box].add(digit)
                    board[row][col] = digit
                    
                    if backtrack(next_row, next_col):
                        return True
                    
                    # unplace digit
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[box].remove(digit)
                    board[row][col] = "."
            
            return False
        
        backtrack(0, 0)