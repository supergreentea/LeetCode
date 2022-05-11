class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        
        def bfs(grid, row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                pixel = queue.popleft()
                for direction in directions:
                    adj = (pixel[0] + direction[0], pixel[1] + direction[1])
                    if 0 <= adj[0] < len(grid) and 0 <= adj[1] < len(grid[0]) and adj not in visited and grid[adj[0]][adj[1]] == '1':
                        queue.append(adj)
                        visited.add(adj)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == '1':
                    count += 1
                    bfs(grid, row, col)
        
        return count
                    
                    
                
        