class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        row_below = triangle[-1]
        for r in range(ROWS - 2, -1, -1):
            cur_row = []
            for c in range(r + 1):
                cur_row.append(triangle[r][c] + min(row_below[c], row_below[c + 1]))
            row_below = cur_row
        return row_below[0]