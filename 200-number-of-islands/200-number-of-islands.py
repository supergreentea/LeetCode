class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    adj = (r + dr, c + dc)
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and adj not in visited and grid[r][c] == '1':
                        queue.append(adj)
                        visited.add(adj)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == '1':
                    count += 1
                    bfs(row, col)
        
        return count
                    
                    
                
        