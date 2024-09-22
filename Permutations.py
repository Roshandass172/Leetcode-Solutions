class Solution:
    def permute(self, nums):
        result = []
        self.backtrack(nums, [], result)
        return result

    def backtrack(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path)
            return
        for i in range(len(nums)):
            if nums[i] in path:  # Skip already used numbers
                continue
            self.backtrack(nums, path + [nums[i]], result)

# Example usage:
s = Solution()
print(s.permute([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(s.permute([0, 1]))     # Output: [[0,1],[1,0]]
print(s.permute([1]))        # Output: [[1]]
