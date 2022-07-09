class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = 0
                    queue = deque([(row, col)])
                    visited.add((row, col))
                    
                    while queue:
                        r, c = queue.popleft()
                        area += 1
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r + dr, c + dc
                            if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                    
                    max_area = max(area, max_area)
        
        return max_area
            