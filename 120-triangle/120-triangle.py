class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        for row in reversed(range(ROWS - 1)):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]