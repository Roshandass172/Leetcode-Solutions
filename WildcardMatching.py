class Solution:
    def isMatch(self, s, p):
        # Initialize a DP table with dimensions (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True

        # Fill the first row for patterns that only consist of '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' can match empty sequence (dp[i][j-1]) or any sequence (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Match single character or '?'
                    dp[i][j] = dp[i - 1][j - 1]

        # The answer will be in the bottom-right corner of the table
        return dp[len(s)][len(p)]

# Example usage:
s = Solution()
print(s.isMatch("aa", "a"))     # Output: False
print(s.isMatch("aa", "*"))     # Output: True
print(s.isMatch("cb", "?a"))    # Output: False
