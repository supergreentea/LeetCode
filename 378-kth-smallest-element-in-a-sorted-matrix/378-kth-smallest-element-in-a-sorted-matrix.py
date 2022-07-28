class Solution:
    
    
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        MIN, MAX = matrix[0][0], matrix[ROWS - 1][COLS - 1]
        
        start, end = MIN, MAX
        
        def count_smaller(mid, smaller, larger):
            count = 0
            row, col = ROWS - 1, 0
            
            while row >= 0 and col < COLS:
                if matrix[row][col] > mid:
                    larger = min(larger, matrix[row][col])
                    row -=1
                else:
                    smaller = max(smaller, matrix[row][col])
                    col += 1
                    count += row + 1
                    
            return count, smaller, larger
        
        while start < end:
            mid = (start + end) // 2
            smaller, larger = MIN, MAX
            count, smaller, larger = count_smaller(mid, smaller, larger)
            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller
        
        return start