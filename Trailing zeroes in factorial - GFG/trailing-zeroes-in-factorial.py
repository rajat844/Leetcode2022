#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	#code here 
    	ans = 0
    	while N:
    	    N = N//5
    	    ans += N
    	
    	return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends