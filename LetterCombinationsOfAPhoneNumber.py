class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def backtrack(index, path):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            # Get the letters that the current digit can represent
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack to try the next letter
        
        combinations = []
        backtrack(0, [])
        return combinations

# Example usage
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(""))    # Output: []
print(sol.letterCombinations("2"))   # Output: ["a","b","c"]
