class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonals, self.antidiagonals = defaultdict(int), defaultdict(int)
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        sign = -1 if player == 1 else 1
        delta = sign * 1
        needed = sign * self.n
        self.rows[row] += delta
        self.cols[col] += delta
        self.diagonals[row + col] += delta
        self.antidiagonals[row - col] += delta
        if self.rows[row] == needed or self.cols[col] == needed or self.diagonals[row + col] == needed or self.antidiagonals[row - col] == needed:
            return player
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)