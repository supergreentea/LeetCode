class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])
        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        def perform_click(row, col):
            num_adjacent_mines = 0
            
            for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                adj_row, adj_col = row + row_offset, col + col_offset
                if 0 <= adj_row < ROWS and 0 <= adj_col < COLS and board[adj_row][adj_col] == 'M':
                    num_adjacent_mines += 1
                
            if num_adjacent_mines == 0:
                board[row][col] = 'B'
                for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    adj_row, adj_col = row + row_offset, col + col_offset
                    if 0 <= adj_row < ROWS and 0 <= adj_col < COLS and board[adj_row][adj_col] == 'E':
                        perform_click(adj_row, adj_col)
            else:
                board[row][col] = str(num_adjacent_mines)
            
            
        perform_click(row, col)
        return board    