class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 2:
            return 1
        
        l, r = 1, x
        
        target = x
        
        while l <= r:
            
            m = (l + r) // 2
            
            square = m * m
            if square == target:
                return m
            if target < square:
                r = m - 1
            elif target > square:
                l = m + 1
        
        return r
            