class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxRows, maxCols = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def bfs(row, col):
            queue = deque([(row, col)])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < maxRows and 0 <= nc < maxCols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        for i in range(maxRows):
            for j in range(maxCols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
        
        return count
                