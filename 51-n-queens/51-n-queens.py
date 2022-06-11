class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols, diag, antidiag = set(), set(), set()
        output = []
        
        def backtrack(row):
            if row == n:
                solution = []
                for r in board:
                    solution.append(''.join(r))
                output.append(solution)
                return
            
            for col in range(n):
                if col in cols or row + col in diag or row - col in antidiag:
                    continue
                
                # place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row + col)
                antidiag.add(row - col)
                
                backtrack(row + 1)
                
                # remove queen
                board[row][col] = '.'
                cols.remove(col)
                diag.remove(row + col)
                antidiag.remove(row - col)
        
        backtrack(0)
        return output