class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # get largest row where first element is smaller than target
        def get_row_to_search():
            lo, hi = 0, ROWS - 1
            while lo <= hi:
                middle = (lo + hi) // 2
                if matrix[middle][0] <= target:
                    if middle + 1 >= ROWS:
                        return middle
                    if matrix[middle + 1][0] > target:
                        return middle
                    lo = middle + 1
                else:
                    hi = middle - 1
            return -1
        
        # try to find target in row
        def find_target_in_row(row):
            lo, hi = 0, COLS - 1
            while lo <= hi:
                middle = (lo + hi) // 2
                if target == matrix[row][middle]:
                    return middle
                elif target < matrix[row][middle]:
                    hi = middle - 1
                else:
                    lo = middle + 1
            return -1
                    
        row_to_search = get_row_to_search()
        if row_to_search == -1: # target is smaller than all elements in matrix
            return False
        
        return find_target_in_row(row_to_search) != -1
        
                    