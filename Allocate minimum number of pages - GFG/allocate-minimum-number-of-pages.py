class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        def isValid(x):
            temp = 0
            st = 1
            
            for i in range(n):
                temp += A[i]
                if temp > x:
                    st += 1
                    temp = A[i]
                    if st > M or temp > x:
                        return False
            return True
            
        #code here
        l = 0
        h = sum(A)
        
        while l <= h:
            mid = (l+h) >> 1
            
            if isValid(mid):
                h = mid - 1
            else:
                l = mid + 1
        
        return l


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends