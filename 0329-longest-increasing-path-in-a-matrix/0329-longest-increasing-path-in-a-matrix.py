class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        ans = 1
        
        @cache
        def longestPath(row: int, col: int) -> int:
            longest = 1
            visited.add((row, col))
            for rowOffset, colOffset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS and matrix[newRow][newCol] > matrix[row][col] and (newRow, newCol) not in visited:
                    longest = max(longest, 1 + longestPath(newRow, newCol))
            visited.remove((row, col))
            return longest
        
        for row in range(ROWS):
            for col in range(COLS):
                ans = max(ans, longestPath(row, col))
        
        return ans
                    