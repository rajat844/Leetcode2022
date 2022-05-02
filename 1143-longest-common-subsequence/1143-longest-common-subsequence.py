class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        dp = [[-1 for i  in range(n2+1)]for j in range(n1+1)]
        
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
                else:
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                        
                    else :
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                        
        
        i = n1 
        j = n2
        
        s = ''
        
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                s += text1[i-1]
                i = i-1
                j = j-1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i = i-1
                else:
                    j = j-1
        s = s[::-1]            
        print(s)
            

        return dp[n1][n2]
                        
        