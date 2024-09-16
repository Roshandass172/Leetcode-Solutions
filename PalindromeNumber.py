class Solution:
    def isPalindrome(self, x):
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        
        original = x
        reversed_number = 0
        
        while x > 0:
            digit = x % 10
            x //= 10
            # Check for overflow
            if reversed_number > (2**31 - 1 - digit) // 10:
                return False
            reversed_number = reversed_number * 10 + digit
        
        return original == reversed_number

# Example usage
sol = Solution()
print(sol.isPalindrome(121))  # Output: true
print(sol.isPalindrome(-121)) # Output: false
print(sol.isPalindrome(10))   # Output: false
