class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])    
        queue = deque()
        fresh = 0
        minutes = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rowOffset, colOffset in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    newRow, newCol = row + rowOffset, col + colOffset
                    # adjacent cell within bounds and has rotten orange
                    if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2 # set current cell rotten
                        queue.append((newRow, newCol))
                        fresh -= 1
        
        return minutes if fresh == 0 else -1