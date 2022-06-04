#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x):
        l = 0
        h = x
        ans = 0
        while l <= h:
            mid = (l+h) >> 1
        
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                ans = mid
                l = mid + 1
            else :
                h = mid - 1
    
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends