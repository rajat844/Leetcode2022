#User function Template for python3
import math 

class Solution:
	def MinSquares(self, n):
		# Code here
		dp = [math.inf for i in range(n+1)]
		
		dp[0] = 0
		dp[1] = 1
		
		for i in range(2,n+1):
		    for j in range(1,int(math.sqrt(i)) + 1):
		        if j * j <= i and dp[i] > dp[i-j*j] + 1:
		            dp[i] = dp[i - j*j] + 1
		
		return dp[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

from math import ceil, sqrt
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.MinSquares(n)
		print(ans)
# } Driver Code Ends