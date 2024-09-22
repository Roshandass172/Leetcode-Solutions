class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])
            if i == current_end:  # Need to make a jump
                jumps += 1
                current_end = farthest

        return jumps

# Example usage:
s = Solution()
print(s.jump([2, 3, 1, 1, 4]))  # Output: 2
print(s.jump([2, 3, 0, 1, 4]))  # Output: 2
