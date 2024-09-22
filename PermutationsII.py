class Solution:
    def permuteUnique(self, nums):
        nums.sort()  # Sort to handle duplicates
        result = []
        self.backtrack(nums, [], [False] * len(nums), result)
        return result

    def backtrack(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the current path
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue  # Skip used elements
            
            # Skip duplicates: if the current element is the same as the previous and the previous wasn't used
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, path, used, result)
            path.pop()  # Backtrack
            used[i] = False  # Mark as unused

# Example usage:
s = Solution()
print(s.permuteUnique([1, 1, 2]))  # Output: [[1,1,2],[1,2,1],[2,1,1]]
print(s.permuteUnique([1, 2, 3]))   # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
