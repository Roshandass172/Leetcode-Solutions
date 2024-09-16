class Solution:
    def removeDuplicates(self, nos):
        if len(nos) == 0:
            return 0
        
        k = 1  # Unique element count. This must be initialized in order to track the position where the next unique element is to be placed in the array
        for i in range(1, len(nos)):
            if nos[i] != nos[i - 1]:
                nos[k] = nos[i]
                k += 1
        
        return k
