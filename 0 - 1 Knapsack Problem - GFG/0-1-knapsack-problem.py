#User function Template for python3
class Solution:        
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for i in range(W+1)] for j in range(n+1)]
        # code here
        def helper(W,n):
            if W == 0 or n == 0:
                return 0
            
            if dp[n][W] != -1:
                return dp[n][W]
                
            elif wt[n-1] > W :
                dp[n][W] = helper(W,n-1)
                return dp[n][W]
            else:
                dp[n][W] =  max(val[n-1] + helper(W-wt[n-1],n-1),helper(W,n-1))
                return dp[n][W]
            
        

        return helper(W,n)

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