class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(row, col):
            nonlocal islands
            islands += 1
            queue = deque([(row, col)])
            visited.add((row, col))
            
            while queue:
                cur_row, cur_col = queue.popleft()
                for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = cur_row + row_offset, cur_col + col_offset
                    if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    
        return islands