class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            newRow = [1]
            a, b = 0, 1
            prevRow = ans[-1]
            while b < len(prevRow):
                newRow.append(prevRow[a] + prevRow[b])
                a += 1
                b += 1
            newRow.append(1)
            ans.append(newRow)
        return ans
                