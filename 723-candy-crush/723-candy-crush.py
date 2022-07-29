class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        
        todo = False
        
        # mark horizontally candies
        for row in range(ROWS):
            for col in range(COLS - 2):
                if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]) != 0:
                    board[row][col] = board[row][col + 1] = board[row][col + 2] = -abs(board[row][col])
                    todo = True
        
        # mark vertical candies
        for row in range(ROWS - 2):
            for col in range(COLS):
                if abs(board[row][col]) == abs(board[row + 1][col]) == abs(board[row + 2][col]) != 0:
                    board[row][col] = board[row + 1][col] = board[row + 2][col] = -abs(board[row][col])
                    todo = True
        
        # crush candies
        for col in range(COLS):
            write_head = ROWS - 1
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] > 0:
                    board[write_head][col] = board[row][col]
                    write_head -= 1
            
            for write_head in range(write_head, -1, -1):
                board[write_head][col] = 0
        
        return self.candyCrush(board) if todo else board