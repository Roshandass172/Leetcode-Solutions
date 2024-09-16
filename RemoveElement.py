class Solution:
    def removeElement(self, nums, val): # Declare function and pass parameters.
        k = 0  # This is a pointer initialized for the elements not equal to val.
        for i in range(len(nums)): # Start a loop over each index of the array nums and check whether the element at that index is not equal to val
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 

