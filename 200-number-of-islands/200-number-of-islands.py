class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        maxRows, maxCols = len(grid), len(grid[0])
        
        def bfs(row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = deque([(row, col)])
            visited.add((row, col))
            
            while queue:
                currow, curcol = queue.popleft()
                for d in directions:
                    adjrow, adjcol = currow + d[0], curcol + d[1]
                    if 0 <= adjrow < maxRows and 0 <= adjcol < maxCols and grid[adjrow][adjcol] == '1' and (adjrow, adjcol) not in visited:
                        queue.append((adjrow, adjcol))
                        visited.add((adjrow, adjcol))
        
        for row in range(maxRows):
            for col in range(maxCols):
                if (row, col) not in visited and grid[row][col] == '1':
                    bfs(row, col)
                    count += 1
        
        return count
                
                