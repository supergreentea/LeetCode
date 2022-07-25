class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        efforts = [[math.inf for col in range(COLS)] for row in range(ROWS)]
        efforts[0][0] = 0
        
        def get_valid_neighbors(row, col):
            valid_neighbors = []
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_row, neighbor_col = row + row_offset, col + col_offset
                if neighbor_row >= 0 and neighbor_row < ROWS and neighbor_col >= 0 and neighbor_col < COLS:
                    valid_neighbors.append((neighbor_row, neighbor_col))
            return valid_neighbors
            
        
        PQ = [(0, 0, 0)]
        while PQ:
            current_effort, row, col = heappop(PQ)
            if current_effort > efforts[row][col]:
                continue
            for neighbor_row, neighbor_col in get_valid_neighbors(row, col):
                new_effort = max(current_effort, abs(heights[row][col] - heights[neighbor_row][neighbor_col]))
                if new_effort < efforts[neighbor_row][neighbor_col]:
                    efforts[neighbor_row][neighbor_col] = new_effort
                    heappush(PQ, (new_effort, neighbor_row, neighbor_col))
        
        return efforts[ROWS - 1][COLS - 1]
            
                    
            