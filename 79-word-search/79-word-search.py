class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        visited = set()
        
        def backtrack(row, col, word_index):
            if word_index == len(word):
                return True
            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[word_index] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            for row_offset, col_offset in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                adj_row, adj_col = row + row_offset, col + col_offset
                if backtrack(adj_row, adj_col, word_index + 1):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        
        return False