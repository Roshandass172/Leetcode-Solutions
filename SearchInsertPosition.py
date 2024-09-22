class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

# Example usage
s = Solution()
print(s.searchInsert([1,3,5,6], 5))  # Output: 2
print(s.searchInsert([1,3,5,6], 2))  # Output: 1
print(s.searchInsert([1,3,5,6], 7))  # Output: 4
