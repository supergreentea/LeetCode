class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        index = 0
        visited = set()
        
        def withinBounds(row: int, col: int) -> bool:
            return row >= 0 and row < ROWS and col >= 0 and col < COLS
        
        
        def backtrack(index: int, row: int, col: int) -> bool:
            if index >= len(word):
                return True
            
            if (row, col) in visited or not withinBounds(row, col) \
                or word[index] != board[row][col]:
                return False
            visited.add((row, col))
            for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if backtrack(index + 1, newRow, newCol):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(0, row, col):
                    return True
        
        return False