class Solution:
    def mySqrt(self, x: int) -> int:
        if (x < 2):
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle
            if square < x:
                left = middle + 1
            elif square > x:
                right = middle - 1
            else:
                return middle
        
        return right
        