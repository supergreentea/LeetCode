class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        
        def backtrack(row, cols, diag, antidiag):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(0, n):
                # place queen in this column
                cur_diag = row - col
                cur_antidiag = row + col
                
                if col in cols or cur_diag in diag or cur_antidiag in antidiag:
                    continue
                
                cols.add(col)
                diag.add(row - col)
                antidiag.add(row + col)
                # recurse on next row with updated state
                backtrack(row + 1, cols, diag, antidiag)
                # remove queen from this column
                cols.remove(col)
                diag.remove(row - col)
                antidiag.remove(row + col)
                
        backtrack(0, set(), set(), set())
        return count
                