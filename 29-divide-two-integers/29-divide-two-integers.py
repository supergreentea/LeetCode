class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT, MIN_INT = 2 ** 31 - 1, -1 * 2 ** 31
        
        # check whether inputs are different signs
        different_signs = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        
        # make signs positive for both 
        if dividend < 0:
            dividend = 0 - dividend
        if divisor < 0:
            divisor = 0 - divisor
        
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