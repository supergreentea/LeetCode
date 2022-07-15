class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(maze), len(maze[0])
        
        def dfs(start_row = start[0], start_col = start[1]):
            if (start_row, start_col) in visited:
                return False
            if [start_row, start_col] == destination:
                return True
            
            visited.add((start_row, start_col))
            
            for d_row, d_col in directions:
                row, col = start_row, start_col    
                while row >= 0 and row < ROWS and col >= 0 and col < COLS and maze[row][col] != 1:
                    row += d_row
                    col += d_col
                if dfs(row - d_row, col - d_col):
                    return True
            
            return False
        
        return dfs()