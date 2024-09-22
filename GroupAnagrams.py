class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for s in strs:
            # Sort the string to find the anagram key
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        
        return list(anagrams.values())

# Example usage:
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagrams([""]))                                   # Output: [[""]]
print(s.groupAnagrams(["a"]))                                  # Output: [["a"]]
