class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        ROWS, COLS = len(mat), len(mat[0])
        
        diagonal_index = 0
        for row in range(ROWS):
            for col in range(COLS):
                diagonals[row + col].append(mat[row][col])
        
        ans = []
        
        for diagonal, elements in diagonals.items():
            if diagonal % 2 == 1:
                for element in elements:
                    ans.append(element)
            else:
                for i in range(len(elements) - 1, -1, -1):
                    ans.append(elements[i])
                    
        return ans
                