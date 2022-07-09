class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        end_square = (-1, -1)
        start_square = (-1, -1)
        obstacles = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    end_square = (row, col)
                if grid[row][col] == 1:
                    start_square = (row, col)
                if grid[row][col] == -1:
                    obstacles += 1

        target = ROWS * COLS - obstacles
        ans = 0

        def backtrack(row, col, squares_visited):
            nonlocal ans
            if (row, col) == end_square and squares_visited + 1 == target:
                ans += 1
                return

            visited.add((row, col))
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + row_offset, col + col_offset
                if next_row >= 0 and next_row < ROWS and next_col >= 0 and next_col < COLS and (next_row, next_col) not in visited and grid[next_row][next_col] != -1:
                    backtrack(next_row, next_col, squares_visited + 1)
            visited.remove((row, col))
        
        backtrack(start_square[0], start_square[1], 0)
        return ans
        