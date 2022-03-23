#User function Template for python3
import sys
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        # def helper(i,j):
        #     if i >= j :
        #         return 0
            
        #     ans = sys.maxsize
            
        #     for k in range(i,j):
        #         x = helper(i,k)
        #         y = helper(k+1,j)
                
        #         temp = x + y + arr[i-1] * arr[k] * arr[j]
        #         ans = min(ans,temp)
            
            
        #     return ans
        
        # return helper(1,len(arr) - 1)
        
        dp = [[-1 for i in range(N)]for j in range(N)]
        
        for i in range(N):
            dp[i][i] = 0
        
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                
                ans = sys.maxsize   
                for k in range(i,j):
                    x = dp[i][k]
                    y = dp[k+1][j]
                    temp = x + y + arr[i-1]*arr[j] *arr[k]
                    ans = min(temp,ans)
                    
                dp[i][j] = ans
        
        return dp[1][N-1]
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