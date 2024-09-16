class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to help avoid duplicates and use two pointers
        n = len(nums)
        quadruplets = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second number
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

# Example usage
sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(sol.fourSum([2, 2, 2, 2, 2], 8))       # Output: [[2,2,2,2]]

