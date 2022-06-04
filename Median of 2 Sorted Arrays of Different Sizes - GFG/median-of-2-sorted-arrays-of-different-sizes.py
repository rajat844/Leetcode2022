#User function Template for python3
import math
class Solution:
    def MedianOfArrays(self, arr1, arr2):
            #code here
            if len(arr1) > len(arr2):
                return self.MedianOfArrays(arr2,arr1)
            
            n1 = len(arr1)
            n2 = len(arr2)
            
            l = 0
            h = n1
            
            while l <= h:
                cut1 = (l+h) >> 1
                cut2 = ((n1+n2+1)>>1) - cut1
                
                l1 = arr1[cut1-1] if cut1 != 0 else -math.inf
                l2 = arr2[cut2-1] if cut2 != 0 else -math.inf
                
                r1 = arr1[cut1] if cut1 != n1 else math.inf
                r2 = arr2[cut2] if cut2 != n2 else math.inf
                
                if l1 <= r2 and l2 <= r1:
                    if (n1+n2)%2 == 0:
                        x = (min(r1,r2)+max(l1,l2))/2
                        if x == int(x):
                            return int(x)
                        else :
                            return x
                    else:
                        return max(l1,l2)
                elif l1 >= r2:
                    h = cut1 - 1
                else :
                    l = cut1 + 1
            
            return -1

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends