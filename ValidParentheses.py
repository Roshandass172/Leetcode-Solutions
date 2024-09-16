class Solution:
    def isValid(self, s):
        # Dictionary to hold the mappings of closing and opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        # Iterate through the string
        for char in s:
            if char in bracket_map:
                # Pop the topmost element of the stack if it exists, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # If the popped element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))        # Output: True
print(sol.isValid("()[]{}"))    # Output: True
print(sol.isValid("(]"))        # Output: False
