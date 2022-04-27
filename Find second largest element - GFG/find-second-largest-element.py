class Solution:
    def print2largest(self,A,N): 
        #code here
        first = -1
        second = -1
        
        for i in range(N):
            if A[i] > first:
                second = first
                first  = A[i]
            elif A[i] > second and A[i] != first:
                second = A[i]
        
        return second


#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.print2largest(a,n))
# } Driver Code Ends