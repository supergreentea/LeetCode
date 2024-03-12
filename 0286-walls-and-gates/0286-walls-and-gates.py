class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            for rowOffset, colOffset in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if (newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS) \
                    and rooms[newRow][newCol] == INF:
                        rooms[newRow][newCol] = rooms[row][col] + 1
                        queue.append((newRow, newCol))
                        
                    
        