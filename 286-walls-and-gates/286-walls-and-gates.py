class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS, EMPTY = len(rooms), len(rooms[0]), 2 ** 31 - 1
        queue = deque()
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            cur_row, cur_col = queue.popleft()
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = cur_row + row_offset, cur_col + col_offset
                if next_row < 0 or next_row >= ROWS or next_col < 0 or next_col >= COLS or rooms[next_row][next_col] != EMPTY:
                    continue
                rooms[next_row][next_col] = rooms[cur_row][cur_col] + 1
                queue.append((next_row, next_col))
                