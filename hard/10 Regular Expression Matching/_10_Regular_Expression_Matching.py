# Problem Name: Two Sum
# Difficulty: Hard
# Problem: https://leetcode.com/problems/regular-expression-matching/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1 )]
        dp[0][0] = True

        for i in range(2,len(p)+1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i-2]
        
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]

        