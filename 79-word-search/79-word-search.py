class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or word[i] != board[r][c]:
                return False
            
            visited.add((r, c))
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
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
            
            