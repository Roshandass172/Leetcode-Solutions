class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the candidates to help skip duplicates
        result = []

        def backtrack(start, combination, remaining):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                combination.append(candidates[i])
                backtrack(i + 1, combination, remaining - candidates[i])  # Move to the next number
                combination.pop()  # Backtrack

        backtrack(0, [], target)
        return result

# Example usage:
s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))  # Output: [[1, 1, 6], [1, 2, 5], [2, 6], [7]]
print(s.combinationSum2([2, 5, 2, 1, 2], 5))         # Output: [[1, 2, 2], [5]]
