#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for i in range(W+1)]for j in range(n+1)]
        
        # def helper(n,W):
        #     if n == 0 or W == 0:
        #         return 0
                
        #     if dp[n][W] != -1:
        #         return dp[n][W]
                
        #     if W < wt[n-1]:
        #         dp[n][W] = helper(n-1,W)
        #         return dp[n][W]
                
        #     else :
        #         dp[n][W] = max(helper(n-1,W) , val[n-1] + helper(n-1,W-wt[n-1]))
        #         return dp[n][W]
                
        # return helper(n,W)
        
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                
        for i in range(1,n+1):
            for j in range(1,W+1):
                if j < wt[i-1]:
                    dp[i][j] = dp[i-1][j]
                else :
                    dp[i][j] = max(dp[i-1][j] , val[i-1] + dp[i-1][j - wt[i-1]])
                    
        return dp[n][W]
        
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends