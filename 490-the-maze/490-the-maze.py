class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(maze), len(maze[0])
        
        visited = set((start[0], start[1]))
        queue = deque([(start[0], start[1])])
        
        while queue:
            start_row, start_col = queue.popleft()
            if [start_row, start_col] == destination:
                return True
            for d_row, d_col in directions:
                row, col = start_row, start_col
                while row >= 0 and row < ROWS and col >= 0 and col < COLS and maze[row][col] == 0:
                    row += d_row
                    col += d_col
                if (row - d_row, col - d_col) not in visited:
                    visited.add((row - d_row, col - d_col))
                    queue.append((row - d_row, col - d_col))
        
        return False