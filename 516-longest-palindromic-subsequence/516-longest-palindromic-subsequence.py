class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        
        n = len(s)
        
        dp = [[-1 for j in range(n+1)]for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                    
        return dp[n][n]
        