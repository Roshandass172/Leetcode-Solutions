class Solution:
    def reverse(self, x):
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10
            # Check for overflow before updating reversed_x
            if reversed_x > (INT_MAX - digit) // 10:
                return 0
            reversed_x = reversed_x * 10 + digit
        
        return sign * reversed_x

# Example usage
sol = Solution()
print(sol.reverse(123))   # Output: 321
print(sol.reverse(-123))  # Output: -321
print(sol.reverse(120))   # Output: 21
