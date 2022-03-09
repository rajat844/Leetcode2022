#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        first = n-1
        second = 0
        
        while first >= 0 and second <= m-1:
            if arr1[first] > arr2[second]:
                arr1[first],arr2[second] = arr2[second],arr1[first]
                first -= 1
                second += 1
            else :
                break
        
        arr1.sort()
        arr2.sort()
    


#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends