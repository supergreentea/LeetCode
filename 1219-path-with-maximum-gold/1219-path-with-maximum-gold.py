class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_gold = 0
        
        def backtrack(row, col, gold):
            nonlocal max_gold
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0 or (row, col) in visited:
                return
            
            gold += grid[row][col]
            max_gold = max(gold, max_gold)
            visited.add((row, col))
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                backtrack(new_row, new_col, gold)
            visited.remove((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row, col, 0)
        
        return max_gold