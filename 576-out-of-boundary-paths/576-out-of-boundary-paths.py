class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        ROWS, COLS = m, n
        memo = {}
        
        def dfs(row, col, moves):
            memo_key = (row, col, moves)
            if memo_key in memo:
                return memo[memo_key]
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 1
            if moves >= maxMove:
                return 0
            
            paths = 0
            for move in range(4):
                row_offset, col_offset = directions[move]
                next_row, next_col = row + row_offset, col + col_offset
                paths += dfs(next_row, next_col, moves + 1)
            
            memo[memo_key] = paths % (10 ** 9 + 7)
            return memo[memo_key]
        
        return dfs(startRow, startColumn, 0)
            
            
            
            