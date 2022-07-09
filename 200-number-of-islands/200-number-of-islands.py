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
                    next_row, next_col = cur_row + row_offset, cur_col + col_offset
                    if next_row >= 0 and next_row < ROWS and next_col >= 0 and next_col < COLS and (next_row, next_col) not in visited and grid[next_row][next_col] == '1':
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == '1':
                    bfs(row, col)
        
        return islands
                