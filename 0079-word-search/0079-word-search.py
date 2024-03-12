class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        wordIndex = 0
        visited = set()
        
        def backtrack(wordIndex, row, col):
            if wordIndex == len(word):
                return True
            if not (row >= 0 and row < ROWS and col >=0 and col < COLS) or (row, col) in visited or word[wordIndex] != board[row][col]:
                return False
            visited.add((row, col))
            for rowOffset, colOffset in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if backtrack(wordIndex + 1, newRow, newCol):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(0, row, col):
                    return True
        
        return False
        