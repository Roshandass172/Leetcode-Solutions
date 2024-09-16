class Solution:
    def intToRoman(self, num):
        # Define the mapping of Roman numerals to corresponding integer values
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = ""
        
        # Loop through each value and its corresponding symbol
        for i in range(len(val)):
            while num >= val[i]:
                roman_numeral += symbols[i]
                num -= val[i]
        
        return roman_numeral

# Example usage
sol = Solution()
print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(sol.intToRoman(58))    # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
