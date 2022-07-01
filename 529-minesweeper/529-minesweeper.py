class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        
        def on_board(row, col):
            return row >= 0 and row < ROWS and col >= 0 and col < COLS
        
        def reveal(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            
            if board[row][col] == 'E':
                num_mines = 0
                for row_offset, col_offset in adjacent:
                    adj_row, adj_col = row + row_offset, col + col_offset
                    if on_board(adj_row, adj_col) and board[adj_row][adj_col] == 'M':
                        num_mines += 1
                if num_mines > 0:
                    board[row][col] = str(num_mines)
                else:
                    board[row][col] = 'B'
                    for row_offset, col_offset in adjacent:
                        adj_row, adj_col = row + row_offset, col + col_offset
                        if on_board(adj_row, adj_col):
                            reveal(adj_row, adj_col)
        
        reveal(click[0], click[1])
        return board