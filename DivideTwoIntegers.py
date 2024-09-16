class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if divisor == 0:
            raise ValueError("Divisor cannot be 0")
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += count
                temp <<= 1
                count <<= 1
        
        quotient = -quotient if negative else quotient
        
        return min(max(INT_MIN, quotient), INT_MAX)
