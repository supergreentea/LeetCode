class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        index = 0
        visited = set()
        N = len(word)
        
        def withinBounds(row: int, col: int) -> bool:
            return row >= 0 and row < ROWS and col >= 0 and col < COLS
        
        def search(index: int, row: int, col: int) -> bool:
            if index == N:
                return True
            
            if not withinBounds(row, col) or (row, col) in visited or board[row][col] != word[index]:
                return False
            
            visited.add((row, col))
            for rowOffset, colOffset in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if search(index + 1, newRow, newCol):
                    return True
            visited.remove((row, col))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if search(0, row, col):
                    return True
        
        return False
            