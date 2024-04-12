class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        
        def search(row: int = 0, col: int = 0, wordIndex: int = 0) -> bool:
            if wordIndex == len(word):
                return True
            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[wordIndex] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if search(newRow, newCol, wordIndex + 1):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if search(row, col, 0):
                    return True
        
        return False