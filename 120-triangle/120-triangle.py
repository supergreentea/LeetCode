class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        for r in range(1, ROWS):
            n = len(triangle[r])
            triangle[r][0] += triangle[r-1][0]
            triangle[r][n-1] += triangle[r-1][n-2]
            for i in range(1, n - 1):
                triangle[r][i] += min(triangle[r-1][i], triangle[r-1][i-1])
        return min(triangle[-1])