class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        if numRows == 1:
            return output
        output.append([1, 1])
        if numRows == 2:
            return output
        
        for row in range(3, numRows + 1):
            cur = [1]
            prev_row = output[-1]
            for i in range(1, row - 1):
                cur.append(prev_row[i - 1] + prev_row[i])
            cur.append(1)
            output.append(cur)
        
        return output