class Solution:
    def myAtoi(self, s):
        # Define 32-bit integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Trim leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Initialize sign and result
        sign = 1
        result = 0
        index = 0
        
        # Determine sign
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        # Convert digits to number
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1
        
        return sign * result

# Example usage
sol = Solution()
print(sol.myAtoi("42"))            # Output: 42
print(sol.myAtoi("   -042"))       # Output: -42
print(sol.myAtoi("1337c0d3"))      # Output: 1337
print(sol.myAtoi("0-1"))           # Output: 0
print(sol.myAtoi("words and 987")) # Output: 0
