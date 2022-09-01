class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:        
        n = len(s)
        dp = [[0 for i in range(n)]for j in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i > j :
                    continue
                elif i == j:
                    dp[i][j] = 1
                elif s[i] != s[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                else:
                    first = i+1
                    while first < j and s[first] != s[i]:
                        first += 1
                        
                    last = j - 1
                    while last > i and s[last] != s[j]:
                        last -= 1
                
                    if first == j:
                        dp[i][j] =  2*dp[i+1][j-1] + 2
                    elif first == last:
                        dp[i][j] =  2*dp[i+1][j-1] + 1
                    else:
                        dp[i][j] =  2*dp[i+1][j-1] - dp[first+1][last-1]
                
        return dp[0][n-1] % (10**9 + 7)
    