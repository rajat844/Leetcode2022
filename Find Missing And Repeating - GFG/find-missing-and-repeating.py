#User function Template for python3

class Solution:
    def findTwoElement( self,A, n): 
        # code here
        n = len(A)
        S = (n*(n+1))/2
        P = (n*(n+1)*(2*n+1))/6

        for i in range(n):
            S -= A[i]
            P -= A[i] * A[i]

        missing = int((S +(P/S))/2)
        repeating = int(missing - S)

        return [repeating,missing]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends