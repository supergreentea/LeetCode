class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        ROWS, COLS = len(maze), len(maze[0])
        
        def dfs(start_row, start_col):
            if [start_row, start_col] == destination:
                return True
            if (start_row, start_col) in visited:
                return False
            
            visited.add((start_row, start_col))
            
            # go right
            col = start_col
            while col + 1 < COLS and maze[start_row][col + 1] != 1:
                col += 1
            if dfs(start_row, col):
                return True
            
            # go left
            col = start_col
            while col - 1 >= 0 and maze[start_row][col - 1] != 1:
                col -= 1
            if dfs(start_row, col):
                return True
            
            # go down
            row = start_row
            while row + 1 < ROWS and maze[row + 1][start_col] != 1:
                row += 1
            if dfs(row, start_col):
                return True
            
            # go up
            row = start_row
            while row - 1 >= 0 and maze[row - 1][start_col] != 1:
                row -= 1
            if dfs(row, start_col):
                return True
            
            return False
                
        return dfs(start[0], start[1])
                
            
            