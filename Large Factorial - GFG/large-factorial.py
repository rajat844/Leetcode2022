#User function Template for python3
class Solution:

	def factorial(self,a, n):
    	# code here
    	mod = 10**9 + 7
    	
    	m = max(a)
    	st = [1 for i in range(m+1)]
    	
    	for i in range(1,m+1):
    	    st[i] = st[i-1] * i
    	    st[i] = st[i] % mod
    	
    	ans = []
    	for i in range(n):
    	    ans.append(st[a[i]] % mod)
    	
    	return ans
    	
    	


#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        a=list(map(int , input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i,end=" ")
        print()
        tc=tc-1
# } Driver Code Ends