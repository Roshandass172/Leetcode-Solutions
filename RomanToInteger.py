class Solution:
    def romanToInt(self, s):
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the string from left to right
        for char in s:
            current_value = roman_to_int[char]
            # If the current value is greater than the previous value, subtract twice the previous value
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

# Example usage
sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
