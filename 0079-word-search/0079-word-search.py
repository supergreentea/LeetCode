class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        wordIndex = 0
        
        def wordSearch(wordIndex: int, row: int, col: int) -> bool:
            if wordIndex >= len(word):
                return True
            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or word[wordIndex] != board[row][col] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if wordSearch(wordIndex + 1, newRow, newCol):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if wordSearch(0, row, col):
                    return True
        
        return False
            