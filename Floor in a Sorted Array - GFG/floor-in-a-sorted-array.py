class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,N,X):
        #Your code here
        l = 0
        h = N-1
        
        while l <= h:
            mid = (l+h) >> 1
            
            if arr[mid] == X:
                return mid
            elif arr[mid] < X:
                l = mid + 1
            else:
                h = mid - 1
        
        return h
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends