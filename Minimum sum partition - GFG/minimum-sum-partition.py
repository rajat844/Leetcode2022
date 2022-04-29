#User function Template for python3\
import sys
class Solution:
	def minDifference(self, nums, n):
		# code here        
        s = sum(nums)
        dp = [[False for i in range(s+1)]for j in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1,n+1):
            for j in range(1,s+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
		            
        ans = sys.maxsize
        for i in range(s//2,-1,-1):
            if dp[n][i] == True:
                ans = min(ans,s-2*i)
        
        return ans
		        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends