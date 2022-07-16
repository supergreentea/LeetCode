class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        def get_box(row, col):
            return row // 3 * 3 + col // 3
        
        ROWS, COLS = len(board), len(board[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                char = board[row][col]
                box = get_box(row, col)
                if char == ".":
                    continue
                if (char in rows[row]) or (char in cols[col]) or (char in boxes[box]):
                    return False
                rows[row].add(char)
                cols[col].add(char)
                boxes[box].add(char)
        
        return True