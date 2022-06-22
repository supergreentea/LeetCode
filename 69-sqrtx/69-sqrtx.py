class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        
        while low <= high:
            mid = (low + high) // 2
            
            square = mid * mid
            
            if square == x:
                return mid
            if square < x:
                low = mid + 1
            elif square > x:
                high = mid - 1
        
        return high