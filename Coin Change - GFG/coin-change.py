#User function Template for python3

class Solution:
    def count(self, arr, m, n): 
        # code here 
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
        
        for j in range(n+1):
            dp[0][j] = 0
        
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if j >= arr[i-1]:
                    dp[i][j] = dp[i][j-arr[i - 1]] + dp[i-1][j]
                else :
                    dp[i][j] = dp[i-1][j]
                    
                    
        return dp[m][n]
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends