class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]
        if numRows == 1:
            return triangle[:1]
        if numRows == 2:
            return triangle
        for row in range(3, numRows + 1):
            prevRow = triangle[-1]
            curRow = [1]
            for j in range(1, len(prevRow)):
                curRow.append(prevRow[j] + prevRow[j - 1])
            curRow.append(1)
            triangle.append(curRow)
        return triangle