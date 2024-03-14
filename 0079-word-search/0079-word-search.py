class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def backtrack(index: int, row: int, col: int):
            if index == len(word):
                return True
            
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS) or \
                (row, col) in visited or \
                board[row][col] != word[index]:
                return False
            visited.add((row, col))
            for rowOffset, colOffset in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
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