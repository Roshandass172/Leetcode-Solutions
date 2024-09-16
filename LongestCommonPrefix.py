class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first word as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the array
        for s in strs[1:]:
            # Update the prefix to match the current string
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
