class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # Initialize DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Fill first row for patterns that can match an empty string
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]  # Consider '*' as matching zero of the preceding element
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]  # Consider '*' as matching one or more of the preceding element
        
        return dp[m][n]

# Example usage
sol = Solution()
print(sol.isMatch("aa", "a"))    # Output: False
print(sol.isMatch("aa", "a*"))   # Output: True
print(sol.isMatch("ab", ".*"))   # Output: True
