#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		n = len(s1)
		m = len(s2)
		
		dp  = [[-1 for j in range(m+1)]for i in range(n+1)]
		
		
		for i in range(n+1):
		    for j in range(m+1):
		        if i == 0 or j == 0:
		            dp[i][j] = 0
		        
		        elif s1[i-1]==s2[j-1]:
		            dp[i][j] = dp[i-1][j-1]+1
		        else:
		            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		            
		ans = n - dp[n][m] + m - dp[n][m]
		return ans
		       
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends