class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        triangle = [[1], [1, 1]]
        for row in range(3, numRows + 1):
            prev_row = triangle[-1]
            cur_row = [1]
            for i in range(1, row - 1):
                cur_row.append(prev_row[i - 1] + prev_row[i])
            cur_row.append(1)
            triangle.append(cur_row)
        return triangle
