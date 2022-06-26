class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        cols = [0] * 3
        rows = [0] * 3
        diag = 0
        antidiag = 0
        for turn in range(len(moves)):
            row, col = moves[turn]
            delta = 1 if turn % 2 == 0 else -1
            rows[row] += delta
            cols[col] += delta
            if row == col:
                diag += delta
            if col == (2 - row):
                antidiag += delta
            target = delta * 3
            if rows[row] == target or cols[col] == target or diag == target or antidiag == target:
                return "A" if turn % 2 == 0 else "B"
        return "Draw" if len(moves) == 9 else "Pending"
