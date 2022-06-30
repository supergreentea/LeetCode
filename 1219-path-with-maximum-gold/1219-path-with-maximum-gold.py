class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_gold = 0
        visited = set()
        
        def backtrack(row, col, gold):
            if row < 0 or row >= ROWS or \
               col < 0 or col >= COLS or \
               (row, col) in visited or \
               grid[row][col] == 0:
                return
            nonlocal max_gold
            gold += grid[row][col]
            max_gold = max(max_gold, gold)
            visited.add((row, col))
            for row_offset, col_offset in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + row_offset, col + col_offset
                backtrack(next_row, next_col, gold)
            visited.remove((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row, col, 0)
        
        return max_gold