class Solution:
    def searchRange(self, nums,target):
        def find_position(left):
            low, high = 0, len(nums) - 1
            pos = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    pos = mid
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1
            return pos
        
        start = find_position(True)
        if start == -1:
            return [-1, -1]
        end = find_position(False)
        return [start, end]

# Example usage
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(s.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(s.searchRange([], 0))              # Output: [-1, -1]

