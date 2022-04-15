#User function Template for python3
class Solution:
    def countStrings(self,n):
        z = 1
        o = 0
    	for i in range(1,n+1):
    	    z,o = z + o, z
    	return (z+o)%1000000007

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends