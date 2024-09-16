class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array to make it easier to find the closest sum
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Check if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust the pointers based on the sum comparison
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match found
        
        return closest_sum

# Example usage
sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(sol.threeSumClosest([0, 0, 0], 1))       # Output: 0
