#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        ans = 0
        
        for i in range(n-1,1,-1):
            j = 0
            k = i-1 
            
            while j < k:
                if arr[j]+arr[k] > arr[i]:
                    ans += k-j 
                    k -= 1
                
                else :
                    j += 1
            
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr,n))

# } Driver Code Ends