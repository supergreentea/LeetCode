class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        servers_in_row = [0] * ROWS
        servers_in_col = [0] * COLS
        
        for row in range(ROWS):
            servers_in_row[row] = sum(grid[row])
        
        for col in range(COLS):
            servers_in_col[col] = sum(grid[row][col] for row in range(ROWS))
        
        count = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (servers_in_row[row] > 1 or servers_in_col[col] > 1):
                    count += 1
        
        return count