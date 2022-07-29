class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        
        todo = False
        
        # mark horizontal candies
        for row in range(ROWS):
            for col in range(COLS - 2):
                if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]) != 0:
                    board[row][col] = board[row][col + 1] = board[row][col + 2] = -abs(board[row][col])
                    todo = True
        
        # mark vertical candies
        for r in range(ROWS - 2):
            for c in range(COLS):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True
        
        # gravity step
        for c in range(COLS):
            wr = ROWS - 1
            for r in range(ROWS - 1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        
        return self.candyCrush(board) if todo else board