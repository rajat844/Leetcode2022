
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        leftmax = 0
        rightmax = 0
        ans = 0
        i = 0
        j = n -1 
        
        while i < j:
            if arr[i] < arr[j]:
                if arr[i] >= leftmax:
                    leftmax = arr[i]
                else :
                    ans += leftmax - arr[i]
                i += 1
            else:
                if arr[j] >= rightmax:
                    rightmax = arr[j]
                else :
                    ans += rightmax - arr[j]
                j -= 1
        
        return ans
                    
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends