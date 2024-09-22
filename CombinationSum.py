class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)  # not i + 1 because we can reuse same elements
                combination.pop()  # backtrack

        backtrack(target, [], 0)
        return result

# Example usage:
s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(s.combinationSum([2, 3, 5], 8))    # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(s.combinationSum([2], 1))          # Output: []
