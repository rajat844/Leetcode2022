#User function Template for python3
import math
class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        def helper(n,k):
            if dp[n][k] != None:
                return dp[n][k]
                
            if n <= 1 or k <= 1:
                dp[n][k] = k
                return dp[n][k]
            
            dp[n][k] = math.inf
            
            for i in range(1,k+1):
                case1 = dp[n-1][i-1] if dp[n-1][i-1] != None else helper(n-1,i-1)
                case2 = dp[n][k-i] if dp[n][k-i] != None else helper(n,k-i)
                
                dp[n][k] = min(dp[n][k],1+max(case1,case2))
            return dp[n][k]
            
        dp = [[None for j in range(k+1)] for i in range(n+1)]
        return helper(n,k)

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
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends