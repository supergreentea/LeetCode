class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def backtrack(r, c, i):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited.add((r, c))
            for r_offset, c_offset in offsets:
                if backtrack(r + r_offset, c + c_offset, i + 1):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        return False
                