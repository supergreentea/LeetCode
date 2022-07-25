class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        scores = [[-math.inf for col in range(COLS)] for row in range(ROWS)]
        scores[0][0] = grid[0][0]

        def get_valid_neighbors(row, col):
            valid_neighbors = []
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS:
                    valid_neighbors.append((new_row, new_col))
            return valid_neighbors
        
        PQ = [(-grid[0][0], 0, 0)]
        while PQ:
            negative_score, row, col = heappop(PQ)
            score = -negative_score
            if score < scores[row][col]:
                continue
            for neighbor_row, neighbor_col in get_valid_neighbors(row, col):
                neighbor_val = grid[neighbor_row][neighbor_col]
                new_score = min(score, neighbor_val)
                if new_score > scores[neighbor_row][neighbor_col]:
                    scores[neighbor_row][neighbor_col] = new_score
                    heappush(PQ, (-new_score, neighbor_row, neighbor_col))
                    
        return scores[ROWS - 1][COLS - 1]
            