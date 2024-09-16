class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to make it easier to skip duplicates and use two pointers
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip the same element to avoid duplicates
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move the left pointer to the right, skipping over duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping over duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result

# Example usage
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0, 1, 1]))              # Output: []
print(sol.threeSum([0, 0, 0]))              # Output: [[0,0,0]]
