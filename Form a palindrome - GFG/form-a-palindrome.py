#User function Template for python3

class Solution:
    def countMin(self, Str):
        # code here
        n = len(Str)
        str2 = Str[::-1]
        
        dp = [[-1 for i in range(n+1)]for j in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif Str[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else :
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        ans = n - dp[n][n]
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends