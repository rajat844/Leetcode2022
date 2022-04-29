#User function Template for python3
import math
class Solution:
    def matrixMultiplication(self, n, arr):
        # code here
        # def helper(l,r):
        #     if l>=r:
        #         return 0
            
        #     ans = math.inf
            
        #     for k in range(l,r):
        #         tempans = helper(l,k) + helper(k+1,r) + arr[l-1] *arr[r]*arr[k]
        #         ans = min(ans,tempans)
            
        #     return ans
        
        # return helper(1,len(arr)-1)
        dp = [[-1 for i in range(n)]for j in range(n)]
        
        for i in range(n-1,0,-1):
            for j in range(n):
                
                if i >= j:
                    dp[i][j] = 0
                else :
                    dp[i][j] = math.inf
                
                    for k in range(i,j):
                        tempans = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[j]*arr[k]
                        dp[i][j] = min(tempans,dp[i][j])
                
        return dp[1][n-1]
                    
                
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends