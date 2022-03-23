#User function Template for python3
class Solution:
	def maxSumIS(self, arr, n):
		# code here
		
		dp = [-1 for i in range(n)]
		
		for i in range(n):
		    dp[i] = arr[i]
		    for j in range(i-1,-1,-1):
		        if arr[i] > arr[j]:
		            dp[i] = max(arr[i] + dp[j] ,dp[i])
		return max(dp)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends