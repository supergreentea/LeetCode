class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(row, col, word_index):
            if word_index == len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or board[row][col] != word[word_index]:
                return False
            
            visited.add((row, col))
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                if backtrack(new_row, new_col, word_index + 1):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        
        return False