#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        
        for i in range(n+1):
            if dp[i][0]:
                dp[i][0] = 0
            
        for j in range(W+1):
            if dp[0][j]:
                dp[0][j] = 0
                
        for i in range(1,n+1):
            for j in range(1,W+1):
                
                if j >= wt[i-1]:
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j] )
                else :
                    dp[i][j] = dp[i-1][j]
        
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