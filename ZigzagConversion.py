class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows for the zigzag pattern
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Build the zigzag pattern
        for char in s:
            rows[current_row] += char
            # Change direction if at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Concatenate rows to get the final string
        return ''.join(rows)

# Example usage
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(sol.convert("A", 1))               # Output: "A"
