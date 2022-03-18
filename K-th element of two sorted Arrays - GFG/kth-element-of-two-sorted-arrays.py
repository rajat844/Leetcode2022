#User function Template for python3
import math
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2,arr1,m,n,k)
        
        l = max(0,k-m)
        h = min(k,n)
        
        while l <= h:
            cut1 = (l+h)>>1
            cut2 = k  - cut1
            
            left1 = -math.inf if cut1 == 0 else arr1[cut1-1]
            left2 = -math.inf if cut2 == 0 else arr2[cut2-1]
            right1 = math.inf if cut1 == n else arr1[cut1]
            right2 = math.inf if cut2 == m else arr2[cut2]
            
            if left1 <= right2 and left2 <= right1:
                return max(left1,left2)
            elif left1 > right2:
                h = cut1 -1
            else :
                l = cut1 + 1
                
        return -1 
            
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends