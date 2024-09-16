class Solution:
    def strStr(self, haystack, needle): # The self parameter refers to the instance of the class. 
        if not needle:
            return 0
        return haystack.find(needle)

