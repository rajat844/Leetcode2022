#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
		def LongestIncreasingSubsequence(arr):
		    n = len(arr)
		    dp = [1 for i in range(n)]
		    
		    for i in range(n):
		        for j in range(i):
		            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
		                dp[i] = dp[j] + 1
		    
		    return dp
	    
	    arr1 = LongestIncreasingSubsequence(nums)
	    arr2 = LongestIncreasingSubsequence(nums[::-1])
	    arr2 = arr2[::-1]
	    
	    mx = 0
	    for i in range(len(nums)):
	        mx = max(arr2[i] + arr1[i] - 1,mx)
	    
	    return mx
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends