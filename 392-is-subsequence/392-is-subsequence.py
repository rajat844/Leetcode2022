class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        dp = [[-1 for j in range(m+1)]for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else :
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return n==dp[n][m]