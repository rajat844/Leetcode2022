#User function Template for python3
import sys
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1 for j in range(N)]for i in range(N)]
        def solve(i,j):
            if i >= j :
                dp[i][j] = 0
                return dp[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
             
            ans = sys.maxsize   
            
            for k in range(i,j):
                temp = solve(i,k) + solve(k+1,j) + arr[i-1] * arr[k] * arr[j]
                
                ans = min(temp,ans)
            
            dp[i][j] = ans
            return dp[i][j]
            
        return solve(1,N-1)

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