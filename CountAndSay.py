class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        # Recursive call to get the previous sequence
        prev_seq = self.countAndSay(n - 1)
        
        result = ""
        count = 1
        
        # Traverse the previous sequence and construct the current sequence
        for i in range(1, len(prev_seq)):
            if prev_seq[i] == prev_seq[i - 1]:
                count += 1
            else:
                result += str(count) + prev_seq[i - 1]
                count = 1
        # Append the last group
        result += str(count) + prev_seq[-1]
        
        return result

# Example usage
s = Solution()
print(s.countAndSay(4))  # Output: "1211"
print(s.countAndSay(1))  # Output: "1"
