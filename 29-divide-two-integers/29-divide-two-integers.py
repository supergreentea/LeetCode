class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT, MIN_INT = 2147483647, -2147483648
        
        different_signs = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        
        if dividend < 0:
            dividend = 0 - dividend
        if divisor < 0:
            divisor = 0 - divisor
        
        s = 0
        quotient = 0
        while dividend >= divisor:
            power_of_two = 1
            value = divisor
            
            while value << 1 < dividend:
                value <<= 1
                power_of_two <<= 1
            
            quotient += power_of_two
            dividend -= value
            
        
        if different_signs:
            quotient = 0 - quotient
            return max(quotient, MIN_INT)
        
        return min(quotient, MAX_INT)
            