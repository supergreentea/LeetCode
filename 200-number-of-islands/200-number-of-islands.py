class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(row, col):
            visited.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for d_r, d_c in directions:
                    n_r, n_c = r + d_r, c + d_c
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c] == '1' and (n_r, n_c) not in visited:
                        visited.add((n_r, n_c))
                        queue.append((n_r, n_c))
        
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        return count